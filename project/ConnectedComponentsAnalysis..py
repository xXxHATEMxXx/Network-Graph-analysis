import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

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

# Add nodes to the graph
G.add_nodes_from(users, bipartite=0)  # Users belong to the first set
G.add_nodes_from(movies, bipartite=1)  # Movies belong to the second set

# Add edges to the graph
for user_id, movie_id, rating in data:
    G.add_edge(user_id, movie_id, weight=rating)

# Perform connected components analysis
components = list(nx.connected_components(G))

# Plot the connected components
pos = nx.spring_layout(G)  # Define the layout for the visualization

plt.figure(figsize=(10, 8))
colors = ['r', 'g', 'b', 'y', 'c', 'm']  # Color palette for components

for i, component in enumerate(components):
    component_nodes = G.subgraph(component)
    nx.draw_networkx(
        component_nodes,
        pos=pos,
        node_color=colors[i % len(colors)],
        node_size=200,
        with_labels=False,
        alpha=0.7,
    )

plt.title('Connected Components')
plt.axis('off')
plt.show()