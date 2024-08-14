

class Grid:
    def __init__(self, config):
        self.config = config
        self.grid = [[0 for _ in range(self.config.grid_width)] for _ in range(self.config.grid_height)]
        self.history = GridHistory()

    def get_gameobjs(self):
        gameobjs = []
        for y in range(self.config.grid_height):
            for x in range(self.config.grid_width):
                if self.grid[y][x] != 0:
                    gameobjs.append(self.grid[y][x])
        return gameobjs

    def clear(self):
        self.grid = [[0 for _ in range(self.config.grid_width)] for _ in range(self.config.grid_height)]

    def check_history(self):
        return False
        for grid in self.history.history:
            for x in range(len(grid)):
                for y in range(len(grid[x])):
                    if grid[x][y] != self.grid[y][x]:
                        return False

class GridHistory:
    def __init__(self, max_length=20):
        self.max_length = max_length
        self.history = []

    def add(self, grid):
        self.history.append([[0 for _ in range(len(grid[0]))] for _ in range(len(grid))])
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                self.history[-1][x][y] = 0 if grid[y][x] == 0 else 1
