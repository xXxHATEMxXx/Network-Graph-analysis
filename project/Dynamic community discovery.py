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
for user_id, movie_id, _ in data:
    G.add_edge(user_id, movie_id)

# Perform dynamic community detection using the Infomap algorithm
dynamic_communities = algorithms.infomap(G, timestamps=timestamps)

# Plot the dynamic community detection results
fig, ax = plt.subplots(figsize=(10, 6))
dynamic_communities.plot(ax=ax)

plt.title('Dynamic Community Discovery')
plt.show()