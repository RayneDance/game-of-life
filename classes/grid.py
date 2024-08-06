

class Grid:
    def __init__(self, config):
        self.config = config
        self.grid = [[0 for _ in range(self.config.grid_width)] for _ in range(self.config.grid_height)]
        self.history = GridHistory()


class GridHistory:
    def __init__(self, max_length=20):
        self.max_length = max_length
        self.history = []