from heapq import heappop, heappush
import itertools

def a_star(start, goal):
    def h(puzzle):
        return sum(abs(b % 3 - g % 3) + abs(b//3 - g//3)
                   for b, g in ((puzzle.index(i), goal.index(i)) for i in range(1, 9)))

    def neighbors(puzzle):
        i = puzzle.index(0)
        for d in (-1, 1, -3, 3):
            j = i + d
            if 0 <= j < 9 and (i//3 == j//3 or i % 3 == j % 3):
                new_puzzle = puzzle[:]
                new_puzzle[i], new_puzzle[j] = new_puzzle[j], new_puzzle[i]
                yield new_puzzle

    frontier = [(h(start), 0, start, [])]
    explored = set()
    while frontier:
        _, cost, puzzle, path = heappop(frontier)
        puzzle_tuple = tuple(puzzle)
        if puzzle_tuple in explored:
            continue
        explored.add(puzzle_tuple)
        path = path + [puzzle]
        if puzzle == goal:
            return path
        for neighbor in neighbors(puzzle):
            heappush(frontier, (cost + 1 + h(neighbor), cost + 1, neighbor, path))
    return None

# Example usage
start = [1, 2, 3, 5, 6, 0, 7, 8, 4]
goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
solution = a_star(start, goal)
for step in solution:
    print(step[:3])
    print(step[3:6])
    print(step[6:])
    print()
