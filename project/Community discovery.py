import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import community
# Read the data from the Excel file
df = pd.read_excel('rating.xlsx')

# Extract the user IDs, movie IDs, and ratings from the dataframe
user_ids = df['userId'].tolist()
movie_ids = df['movieId'].tolist()
ratings = df['rating'].tolist()

# Create a list of tuples with (user_id, movie_id, rating)
data = list(zip(user_ids, movie_ids, ratings))

# Create a bipartite graph
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

# Perform community detection using Louvain algorithm
partition = community.best_partition(G)

# Create a new graph with community as node attributes
community_graph = nx.Graph()
for node, comm_id in partition.items():
    community_graph.add_node(node, community=comm_id)

# Add edges to the community graph
for user_id, movie_id, _ in data:
    user_comm = partition[user_id]
    movie_comm = partition[movie_id]
    if user_comm != movie_comm:
        community_graph.add_edge(user_id, movie_id)

# Plot the community graph
pos = nx.spring_layout(community_graph)

plt.figure(figsize=(10, 8))
colors = [partition[node] for node in community_graph.nodes]
nx.draw(community_graph, pos=pos, node_color=colors, node_size=100, with_labels=True)
plt.title('Community Discovery')
plt.show()