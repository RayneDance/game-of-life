import pygame
from . import config, grid, screen, gameobj, structures
from random import randint

class Game:
    def __init__(self):
        self.config = config.Config()
        self.grid = grid.Grid(self.config)
        self.screen = screen.Screen(self.config)
        self.clock = pygame.time.Clock()
        self.running = True
        self.paused = False
        self.rule_start_time = None
        self.rule_elapsed_time = None
        self.reset_time = 10*1000
        self.reset_time_start = 0
        self.reset_time_delta = 0
        self.reset = False

    def run(self):
        while self.running:
            self.clock.tick(self.config.speed)
            self.rule_elapsed_time = pygame.time.get_ticks() - self.rule_start_time
            if self.rule_elapsed_time >= self.config.get_ruleset_time():
                if self.config.cycle:
                    print("Changing rule...")
                    self.config.cycle_rule()
                    print(f"New rule: {self.config.rule}")
                    self.setup()

            self.handle_events()
            if not self.paused:
                self.update()
            self.screen.draw(self.grid.get_gameobjs())

            # Set window title
            pygame.display.set_caption(f"Conway's Game of Life - Rule: {self.config.rule["name"]}({self.config.rule["rulestring"]}) - Speed: {self.config.speed} - Paused: {self.paused}")

    def setup(self):
        self.grid.clear()
        self.rule_start_time = pygame.time.get_ticks()
        self.rule_elapsed_time = 0
        self.reset = False
        self.reset_time_delta = 0
        self.reset_time_start = 0
        if self.config.rule["name"] == "Blinkers":
            print("Displaying blinkers")
            self.display_blinkers()
        else:
            self.generate_random_grid()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    self.config.speed = self.config.default_speed if self.config.speed != self.config.default_speed else self.config.high_speed
                if event.key == pygame.K_F2:
                    self.paused = not self.paused
                if event.key == pygame.K_F3:
                    self.setup()
                if event.key == pygame.K_F4:
                    self.config.cycle_rule()
                if event.key == pygame.K_F5:
                    self.config.set_rule(self.config.Rules.blinkers)

    def generate_random_grid(self):
        start_x = int(self.config.grid_width * 0.1)
        end_x = int(self.config.grid_width * 0.9)
        start_y = int(self.config.grid_height * 0.1)
        end_y = int(self.config.grid_height * 0.9)

        for y in range(start_y, end_y):
            for x in range(start_x, end_x):
                if randint(0, 100) < self.config.spawn_percent:
                    self.grid.grid[y][x] = gameobj.GameObject((x * self.config.cell_size, y * self.config.cell_size))
                else:
                    self.grid.grid[y][x] = 0

    def display_blinkers(self):
        new_structs = [
            structures.Structures.blinker(),
            structures.Structures.toad(),
            structures.Structures.beacon(),
            structures.Structures.pulsar()
        ]

        # Figure out size needed, with 2 grid spaces between each structure
        total_width = 0
        total_height = 0
        for struct in new_structs:
            total_width += struct["size"][0]
            total_height = max(total_height, struct["size"][1])
            total_width += 2 * len(new_structs) - 1

        start_x = int(self.config.grid_width / 2 - total_width / 2)
        start_y = int(self.config.grid_height / 2 - total_height / 2)

        for struct in new_structs:
            for y in range(struct["size"][1]):
                for x in range(struct["size"][0]):
                    if struct["structure"][y][x] == 1:
                        self.grid.grid[start_y + y][start_x + x] = gameobj.GameObject(
                            ((start_x + x) * self.config.cell_size, (start_y + y) * self.config.cell_size)
                        )

            start_x += struct["size"][0] + 6

    def update(self):
        # Simulate based on rule
        new_grid = [[0 for _ in range(self.config.grid_width)] for _ in range(self.config.grid_height)]
        birth_conditions = list(map(int, self.config.rule["rulestring"].split("/")[0][1:]))
        survive_conditions = list(map(int, self.config.rule["rulestring"].split("/")[1][1:]))
        for y in range(self.config.grid_height):
            for x in range(self.config.grid_width):
                neighbors = self.get_neighbors(x, y)
                neighbor_count = len(neighbors)
                if self.grid.grid[y][x] == 0:
                    if neighbor_count in birth_conditions:
                        new_grid[y][x] = gameobj.GameObject(
                            (x * self.config.cell_size, y * self.config.cell_size),
                            color=gameobj.GameObject.interpolate_colors(neighbors)
                        )
                elif neighbor_count not in survive_conditions:
                    new_grid[y][x] = 0
                else:
                    new_grid[y][x] = self.grid.grid[y][x]
        self.grid.grid = new_grid

        if self.reset:
            self.reset_time_delta = pygame.time.get_ticks() - self.reset_time_start

        # Check if grid is in history
        if not self.reset and self.grid.check_history():
            self.reset = True
            self.reset_time_start = pygame.time.get_ticks()
            self.reset_time_delta = 0

        if self.reset and self.reset_time_delta > self.reset_time:
            print("Resetting grid...")
            self.setup()


    def get_neighbors(self, x, y):
        neighbors = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                nx = (x + j) % self.config.grid_width
                ny = (y + i) % self.config.grid_height
                if self.grid.grid[ny][nx] != 0:
                    neighbors.append(self.grid.grid[ny][nx])
        return neighbors
