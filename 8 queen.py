def solve_8queens():
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
                return False
        return True

    def solve(board, row):
        if row == 8:
            result.append(board[:])
            return
        for col in range(8):
            if is_safe(board, row, col):
                board[row] = col
                solve(board, row + 1)

    result = []
    solve([-1] * 8, 0)
    return result

# Example usage
solutions = solve_8queens()
for sol in solutions:
    print(sol)
