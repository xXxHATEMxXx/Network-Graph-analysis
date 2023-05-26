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

# Add edges to the graph
for user_id, movie_id, rating in data:
    G.add_edge(user_id, movie_id, weight=rating)

# Calculate clustering coefficients
user_clustering = nx.clustering(G, nodes=users)
movie_clustering = nx.clustering(G, nodes=movies)

# Plot user clustering coefficients
user_labels = list(user_clustering.keys())
user_values = list(user_clustering.values())

plt.bar(range(len(user_values)), user_values, tick_label=user_labels)
plt.xlabel('Users')
plt.ylabel('Clustering Coefficient')
plt.title('User Clustering Coefficients')
plt.xticks(rotation='vertical')
plt.show()

# Plot movie clustering coefficients
movie_labels = list(movie_clustering.keys())
movie_values = list(movie_clustering.values())

plt.bar(range(len(movie_values)), movie_values, tick_label=movie_labels)
plt.xlabel('Movies')
plt.ylabel('Clustering Coefficient')
plt.title('Movie Clustering Coefficients')
plt.xticks(rotation='vertical')
plt.show()