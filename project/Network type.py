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

for user_id, movie_id, rating in data:
    G.add_edge(user_id, movie_id, weight=rating)

# Determine the network type
if nx.is_bipartite(G):
    network_type = 'Bipartite'
    projection = nx.bipartite.projected_graph(G, users)
else:
    network_type = 'Projection'
    projection = G

# Plot the graph
pos = nx.spring_layout(projection)

plt.figure(figsize=(10, 8))
nx.draw(projection, pos=pos, node_size=100, with_labels=True)
plt.title(f'{network_type} Graph')
plt.show()