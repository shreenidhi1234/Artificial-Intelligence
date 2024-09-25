def tsp_nearest_neighbor(graph, start):
    path = [start]
    nodes = set(graph.keys())
    while len(path) < len(nodes):
        nearest = min((graph[path[-1]][n], n) for n in nodes - set(path))[1]
        path.append(nearest)
    path.append(start)  # returning to the start
    return path

# Example usage
graph = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}
path = tsp_nearest_neighbor(graph, 'A')
print("Path:", path)
