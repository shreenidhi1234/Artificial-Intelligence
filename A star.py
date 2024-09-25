from heapq import heappop, heappush

def a_star(graph, start, goal):
    def h(n):
        # Heuristic function (assuming Euclidean distance for example)
        return abs(goal[0] - n[0]) + abs(goal[1] - n[1])
    
    open_list = [(h(start), 0, start, [])]
    closed_set = set()
    while open_list:
        _, cost, node, path = heappop(open_list)
        if node in closed_set:
            continue
        closed_set.add(node)
        path = path + [node]
        if node == goal:
            return path
        for neighbor, weight in graph.get(node, []):
            heappush(open_list, (cost + weight + h(neighbor), cost + weight, neighbor, path))
    return None

# Example usage
graph = {
    (0, 0): [((0, 1), 1), ((1, 0), 1)],
    (0, 1): [((0, 0), 1), ((1, 1), 1)],
    (1, 0): [((0, 0), 1), ((1, 1), 1)],
    (1, 1): [((1, 0), 1), ((0, 1), 1)]
}
start = (0, 0)
goal = (1, 1)
solution = a_star(graph, start, goal)
print("Path:", solution)
