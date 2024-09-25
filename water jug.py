from collections import deque

def water_jug_problem(capacity1, capacity2, target):
    def is_goal(state):
        return target in state

    def next_states(state):
        a, b = state
        return [(capacity1, b), (a, capacity2), (0, b), (a, 0), (min(a + b, capacity1), b - (min(a + b, capacity1) - a)), (a - (min(a + b, capacity2) - b), min(a + b, capacity2))]

    initial_state = (0, 0)
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()
        if state in visited:
            continue
        visited.add(state)
        path = path + [state]
        if is_goal(state):
            return path
        for ns in next_states(state):
            if ns not in visited:
                queue.append((ns, path))
    return None

# Example usage
capacity1, capacity2, target = 4, 3, 2
solution = water_jug_problem(capacity1, capacity2, target)
for step in solution:
    print(step)
