class VacuumCleaner:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.position = (0, 0)  # starting at the top-left corner

    def clean(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == 1:
                    print(f"Cleaning dirt at ({i}, {j})")
                    self.grid[i][j] = 0
                else:
                    print(f"Position ({i}, {j}) is already clean")

# Example usage
grid = [
    [1, 0, 0],
    [0, 1, 1],
    [1, 1, 0]
]
vacuum = VacuumCleaner(grid)
vacuum.clean()
