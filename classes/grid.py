

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
        # Flatten grid to 1D list
        # Replace all objects with a 1
        flat = [1 if self.grid[y][x] != 0 else 0 for y in range(self.config.grid_height) for x in range(self.config.grid_width)]

        # Check if grid is in history
        if flat in self.history.history:
            return True
        else:
            self.history.add(flat)
            return False

class GridHistory:
    def __init__(self, max_length=20):
        self.max_length = max_length
        self.history = []

    def add(self, grid):
        if len(self.history) >= self.max_length:
            self.history.pop(0)
        self.history.append(grid)
