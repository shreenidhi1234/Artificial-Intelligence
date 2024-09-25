def is_valid(graph, colors, node, color):
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
    return True

def map_coloring(graph, colors, node, available_colors):
    if node == len(graph):
        return True
    for color in available_colors:
        if is_valid(graph, colors, node, color):
            colors[node] = color
            if map_coloring(graph, colors, node + 1, available_colors):
                return True
            colors[node] = None
    return False

# Example usage
graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}
available_colors = ['Red', 'Green', 'Blue']
colors = [None] * len(graph)
if map_coloring(graph, colors, 0, available_colors):
    print("Colors assigned:", colors)
else:
    print("No solution")
