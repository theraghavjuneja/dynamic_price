import osmnx as ox
import networkx as nx
import taxicab as tc

# Load the graph
G = ox.load_graphml("Manhattan.graphml")
origin_coordinates = (40.70195053163349, -74.01123198479581)
destination_coordinates = (40.87148739347057, -73.91517498611597)
route = tc.distance.shortest_path(G, origin_coordinates, destination_coordinates)

# Calculate the shortest path length
shortest_path_length = nx.shortest_path_length(G, route, weight='length')
print("Shortest path length:", shortest_path_length)
