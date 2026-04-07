"""
Build MADE_author_communities_claude.csv using a hand-rolled Louvain
community-detection algorithm, following the approach from Week 6.

Louvain works in two alternating phases until nothing changes:
  Phase 1 – local moves: for every node, check whether moving it into a
             neighbour's community raises modularity; keep the best move.
  Phase 2 – aggregation: collapse each community into a single super-node,
             preserving total edge weight, then repeat Phase 1 on the
             smaller graph.

Modularity (eq. 9.12 from the textbook, generalised to weighted graphs):
  Q = (1/2m) * Σ_{ij} [ A_ij - k_i*k_j / (2m) ] * δ(c_i, c_j)

The gain from moving node i out of its community and into community C is:
  ΔQ = k_{i→C}/m  -  k_i * Σ_tot(C) / (2m²)
where k_{i→C} is the sum of edge weights from i to nodes already in C,
and Σ_tot(C) is the sum of all degrees of nodes in C.
"""

from __future__ import annotations

import ast
import random
from collections import defaultdict
from itertools import combinations
from pathlib import Path

import pandas as pd


# ---------------------------------------------------------------------------
# Graph helpers (dict-of-dicts with float weights, undirected)
# ---------------------------------------------------------------------------

def build_graph(works_df: pd.DataFrame) -> dict[str, dict[str, float]]:
    """Return adjacency dict from author_ids column."""
    adj: dict[str, dict[str, float]] = defaultdict(lambda: defaultdict(float))

    for raw in works_df["author_ids"]:
        if pd.isna(raw):
            continue
        ids = ast.literal_eval(raw)
        # normalise: strip whitespace, add full URL if needed
        clean = []
        for aid in ids:
            aid = str(aid).strip()
            if not aid:
                continue
            if not aid.startswith("https://openalex.org/"):
                aid = f"https://openalex.org/{aid}"
            clean.append(aid)
        # deduplicate while preserving order
        clean = list(dict.fromkeys(clean))

        for a, b in combinations(clean, 2):
            adj[a][b] += 1.0
            adj[b][a] += 1.0

    # ensure every node appears even if it has no edges yet
    # (single-author papers add isolated nodes)
    for raw in works_df["author_ids"]:
        if pd.isna(raw):
            continue
        for aid in ast.literal_eval(raw):
            aid = str(aid).strip()
            if not aid:
                continue
            if not aid.startswith("https://openalex.org/"):
                aid = f"https://openalex.org/{aid}"
            if aid not in adj:
                adj[aid] = defaultdict(float)

    return adj


def node_degree(adj: dict, node) -> float:
    return sum(adj[node].values())


def total_weight(adj: dict) -> float:
    return sum(sum(nbrs.values()) for nbrs in adj.values()) / 2.0


# ---------------------------------------------------------------------------
# Louvain implementation
# ---------------------------------------------------------------------------

class Louvain:
    """
    Hand-rolled Louvain community detection.

    Attributes
    ----------
    community : dict[node, int]
        Final community assignment for original nodes.
    """

    def __init__(self, adj: dict[str, dict[str, float]], seed: int = 42):
        self._rng = random.Random(seed)
        self.community = self._run(adj)

    def _run(self, adj: dict) -> dict:
        """Run full Louvain (multi-level) and return node→community map."""
        # Keep track of how original nodes map to super-nodes across levels.
        # node_to_super[original_node] = current super-node label
        nodes = list(adj.keys())
        node_to_super: dict = {n: n for n in nodes}

        current_adj = adj

        while True:
            # --- Phase 1: local moves on current_adj ---
            partition = self._phase1(current_adj)

            # Check if anything actually merged
            n_communities = len(set(partition.values()))
            if n_communities == len(current_adj):
                # No merges happened; we're done
                break

            # --- Phase 2: aggregate into super-nodes ---
            current_adj = self._phase2(current_adj, partition)

            # Update original-node → super-node mapping
            for orig, sup in node_to_super.items():
                node_to_super[orig] = partition[sup]

            if n_communities == 1:
                break

        # Re-label communities 0, 1, 2, … by descending size
        from collections import Counter
        size = Counter(node_to_super.values())
        label_order = [s for s, _ in size.most_common()]
        relabel = {old: new for new, old in enumerate(label_order)}
        return {n: relabel[c] for n, c in node_to_super.items()}

    # ------------------------------------------------------------------
    # Phase 1 – local modularity optimisation
    # ------------------------------------------------------------------

    def _phase1(self, adj: dict) -> dict[str, str]:
        """
        Assign each node to the neighbour community that maximises ΔQ.
        Repeat until no node moves.
        Returns partition: node → community_label (a node label, not int).
        """
        # Each node starts in its own community
        partition: dict = {n: n for n in adj}

        # community → set of member nodes
        comm_members: dict = {n: {n} for n in adj}

        # Σ_tot(C) = sum of degrees of all nodes in community C
        degrees = {n: node_degree(adj, n) for n in adj}
        sigma_tot: dict = {n: degrees[n] for n in adj}  # keyed by community label

        m = total_weight(adj)
        if m == 0:
            return partition

        nodes = list(adj.keys())

        improved = True
        while improved:
            improved = False
            self._rng.shuffle(nodes)

            for node in nodes:
                k_i = degrees[node]
                current_comm = partition[node]

                # k_{i→C} for every neighbouring community
                k_to: dict[str, float] = defaultdict(float)
                for nbr, w in adj[node].items():
                    k_to[partition[nbr]] += w

                # Remove node from its current community (temporarily)
                sigma_tot[current_comm] -= k_i

                # ΔQ for leaving current community (going to isolated singleton)
                # We compute gain relative to moving to each candidate community.
                # gain(C) = k_{i→C}/m  -  k_i * sigma_tot(C) / (2*m^2)
                # We want the community with maximum gain; include "stay" as option.

                best_comm = current_comm
                # gain of staying = k_{i→current}/m - k_i*sigma_tot_after/(2m²)
                # (sigma_tot already has node removed, so sigma_tot[current_comm]
                #  is the "after removal" value)
                best_gain = (
                    k_to.get(current_comm, 0.0) / m
                    - k_i * sigma_tot[current_comm] / (2 * m * m)
                )

                for comm, k_ic in k_to.items():
                    if comm == current_comm:
                        continue
                    gain = k_ic / m - k_i * sigma_tot[comm] / (2 * m * m)
                    if gain > best_gain:
                        best_gain = gain
                        best_comm = comm

                # Restore sigma_tot before deciding
                sigma_tot[current_comm] += k_i

                if best_comm != current_comm:
                    # Move node
                    comm_members[current_comm].discard(node)
                    sigma_tot[current_comm] -= k_i

                    partition[node] = best_comm
                    comm_members[best_comm].add(node)
                    sigma_tot[best_comm] += k_i

                    improved = True

        return partition

    # ------------------------------------------------------------------
    # Phase 2 – aggregate communities into super-nodes
    # ------------------------------------------------------------------

    @staticmethod
    def _phase2(
        adj: dict,
        partition: dict[str, str],
    ) -> dict[str, dict[str, float]]:
        """
        Build a new graph where each community is a single super-node.
        Edge weights are summed; self-loops are kept (they represent internal
        edges and affect sigma_tot in the next phase).
        """
        new_adj: dict[str, dict[str, float]] = defaultdict(
            lambda: defaultdict(float)
        )
        # Ensure every community label appears as a node, even if isolated
        for comm in set(partition.values()):
            if comm not in new_adj:
                new_adj[comm]  # touch to create the defaultdict entry

        for node, nbrs in adj.items():
            c_node = partition[node]
            for nbr, w in nbrs.items():
                c_nbr = partition[nbr]
                if c_node == c_nbr:
                    # internal edge — only count once per direction to keep
                    # total_weight consistent (we halve in total_weight)
                    new_adj[c_node][c_node] += w / 2.0
                else:
                    new_adj[c_node][c_nbr] += w

        return new_adj


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    script_dir = Path(__file__).resolve().parent

    input_path  = script_dir / "MADE_works.csv"
    output_path = script_dir / "MADE_author_communities_claude.csv"

    print("Loading data …")
    works_df = pd.read_csv(input_path, usecols=["author_ids"])

    print("Building co-authorship graph …")
    adj = build_graph(works_df)
    n_nodes = len(adj)
    n_edges = sum(len(v) for v in adj.values()) // 2
    print(f"  Nodes: {n_nodes},  Edges: {n_edges}")

    print("Running Louvain community detection …")
    louvain = Louvain(adj, seed=42)
    community = louvain.community

    print("Writing results …")
    rows = [
        {
            "author_id": author_id,
            "community": community[author_id],
            "degree": int(node_degree(adj, author_id)),
        }
        for author_id in adj
    ]

    df = pd.DataFrame(rows).sort_values(
        by=["community", "degree", "author_id"],
        ascending=[True, False, True],
    )
    df.to_csv(output_path, index=False)

    n_communities = df["community"].nunique()
    print(f"Saved {len(df)} rows → {output_path}")
    print(f"Communities found: {n_communities}")


if __name__ == "__main__":
    main()
