from collections import deque

def missionaries_cannibals():
    def is_valid(state):
        m, c, b = state
        return 0 <= m <= 3 and 0 <= c <= 3 and (m == 0 or m >= c) and (3 - m == 0 or 3 - m >= 3 - c)

    def next_states(state):
        m, c, b = state
        if b == 1:
            return [(m - 2, c, 0), (m, c - 2, 0), (m - 1, c - 1, 0), (m - 1, c, 0), (m, c - 1, 0)]
        else:
            return [(m + 2, c, 1), (m, c + 2, 1), (m + 1, c + 1, 1), (m + 1, c, 1), (m, c + 1, 1)]

    initial_state = (3, 3, 1)
    goal_state = (0, 0, 0)
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()
        if state in visited:
            continue
        visited.add(state)
        path = path + [state]
        if state == goal_state:
            return path
        for ns in next_states(state):
            if is_valid(ns) and ns not in visited:
                queue.append((ns, path))
    return None

# Example usage
solution = missionaries_cannibals()
for step in solution:
    print(step)
