import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Read the data from Excel
df = pd.read_excel('rating.xlsx')

# Extract the user IDs, movie IDs, and ratings from the dataframe
user_ids = df['userId'].tolist()
movie_ids = df['movieId'].tolist()
ratings = df['rating'].tolist()

# Create a list of tuples with (user_id, movie_id, rating)
data = list(zip(user_ids, movie_ids, ratings))

G = nx.Graph()
users = set()
movies = set()

# Add nodes for users and movies separately
for user_id, movie_id, _ in data:
    users.add(user_id)
    movies.add(movie_id)

# Add nodes to the graph
G.add_nodes_from(users, bipartite=0)  # Users belong to the first set
G.add_nodes_from(movies, bipartite=1)  # Movies belong to the second set

# Add edges to the graph
for user_id, movie_id, rating in data:
    G.add_edge(user_id, movie_id, weight=rating)

# Create a bipartite layout
pos = nx.bipartite_layout(G, users)

# Separate the nodes based on bipartite set
user_nodes = {n for n, d in G.nodes(data=True) if d['bipartite'] == 0}
movie_nodes = set(G) - user_nodes

# Draw the bipartite graph
nx.draw_networkx_nodes(G, pos, nodelist=user_nodes, node_color='b')
nx.draw_networkx_nodes(G, pos, nodelist=movie_nodes, node_color='r')
nx.draw_networkx_edges(G, pos)
plt.axis('off')
plt.show()


