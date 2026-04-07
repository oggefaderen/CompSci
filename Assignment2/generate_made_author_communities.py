from __future__ import annotations

import argparse
import ast
from itertools import combinations
from pathlib import Path

import networkx as nx
import pandas as pd
from networkx.algorithms.community import louvain_communities


def normalize_author_id(author_id: str) -> str:
    if author_id is None or pd.isna(author_id):
        return ""

    author_id = str(author_id).strip()
    if not author_id:
        return ""
    if author_id.lower() in {"none", "nan", "null"}:
        return ""
    if author_id.startswith("https://openalex.org/"):
        return author_id
    return f"https://openalex.org/{author_id}"


def parse_author_ids(raw_value: str) -> list[str]:
    if pd.isna(raw_value):
        return []

    author_ids = ast.literal_eval(raw_value)
    cleaned = []
    for author_id in author_ids:
        normalized = normalize_author_id(author_id)
        if normalized:
            cleaned.append(normalized)

    # Preserve input order but avoid duplicate authors within the same paper.
    return list(dict.fromkeys(cleaned))


def build_graph(works_df: pd.DataFrame) -> nx.Graph:
    graph = nx.Graph()

    for raw_value in works_df["author_ids"]:
        author_ids = parse_author_ids(raw_value)
        if not author_ids:
            continue

        graph.add_nodes_from(author_ids)
        if len(author_ids) < 2:
            continue

        graph.add_edges_from(combinations(author_ids, 2))

    return graph


def community_frame(graph: nx.Graph, seed: int) -> pd.DataFrame:
    communities = louvain_communities(graph, seed=seed)

    # Reindex communities by size for a stable, easy-to-read output.
    ordered_communities = sorted(
        communities,
        key=lambda members: (-len(members), min(members)),
    )

    community_lookup: dict[str, int] = {}
    for community_id, members in enumerate(ordered_communities):
        for author_id in members:
            community_lookup[author_id] = community_id

    rows = [
        {
            "author_id": author_id,
            "community": community_lookup[author_id],
            "degree": degree,
        }
        for author_id, degree in graph.degree()
    ]

    return pd.DataFrame(rows).sort_values(
        by=["community", "degree", "author_id"],
        ascending=[True, False, True],
    )


def main() -> None:
    script_dir = Path(__file__).resolve().parent

    parser = argparse.ArgumentParser(
        description="Generate author communities for MADE_works.csv using Louvain.",
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=script_dir / "MADE_works.csv",
        help="Path to MADE_works.csv",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=script_dir / "MADE_author_communities.csv",
        help="Path to output CSV",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed for Louvain community detection",
    )
    args = parser.parse_args()

    works_df = pd.read_csv(args.input, usecols=["author_ids"])
    graph = build_graph(works_df)
    communities_df = community_frame(graph, seed=args.seed)

    communities_df.to_csv(args.output, index=False)

    print(f"Saved {len(communities_df)} author-community assignments to {args.output}")
    print(f"Nodes: {graph.number_of_nodes()}, Edges: {graph.number_of_edges()}")
    print(
        "Communities:",
        communities_df["community"].nunique(),
        f"(seed={args.seed})",
    )


if __name__ == "__main__":
    main()
