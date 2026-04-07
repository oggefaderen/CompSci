"""
Exactly the same code as Week6/exercise4.ipynb, pointed at MADE_works.csv.
"""
from collections import defaultdict
from community import community_louvain
import networkx as nx
import pandas as pd
import ast

df = pd.read_csv('MADE_works.csv')
df['author_ids'] = df['author_ids'].apply(ast.literal_eval)

def normalize(aid):
    aid = str(aid).strip()
    if not aid.startswith("https://openalex.org/"):
        aid = "https://openalex.org/" + aid
    return aid

G = nx.Graph()
for _, row in df.iterrows():
    authors = row['author_ids']
    for i in range(len(authors)):
        for j in range(i + 1, len(authors)):
            if authors[i] and authors[j]:
                G.add_edge(normalize(authors[i]), normalize(authors[j]))

print(f'Nodes: {G.number_of_nodes()}, Edges: {G.number_of_edges()}')

partition = community_louvain.best_partition(G)

num_communities = max(partition.values()) + 1
print(f'Number of communities: {num_communities}')

modularity = community_louvain.modularity(partition, G)
print(f'Modularity: {modularity:.4f}')

community_df = pd.DataFrame([
    {'author_id': node, 'community': comm}
    for node, comm in partition.items()
])

degree_df = pd.DataFrame([
    {'author_id': node, 'degree': deg}
    for node, deg in G.degree()
])

community_df = community_df.merge(degree_df, on='author_id')
community_df.to_csv('MADE_author_communities_claude.csv', index=False)
print(f'Saved {len(community_df)} rows to MADE_author_communities_claude.csv')
