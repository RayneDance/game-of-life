from enum import Enum
from random import choice
from itertools import cycle

class TimeHelpers(Enum):
    SECOND = 1000
    MINUTE = 1000 * 60
    HOUR = 60 * 60 * 1000
    DAY = 24 * 60 * 60 * 1000


class Rules:
    def __init__(self):
        self.CONWAY = {
            "rulestring": "B3/S23",
            "name": "Conway's Game of Life",
            "ruletime": 10 * TimeHelpers.MINUTE.value
        }
        self.HIGH_LIFE = {
            "rulestring": "B23/S36",
            "name": "High Life",
            "ruletime": 0 * TimeHelpers.SECOND.value
        }
        self.DAY_NIGHT = {
            "rulestring": "B3678/S34678",
            "name": "Day/Night",
            "ruletime": 0 * TimeHelpers.SECOND.value
        }
        self.MAZE = {
            "rulestring": "B3/S12345",
            "name": "Maze",
            "ruletime": 10 * TimeHelpers.SECOND.value
        }
        self.MAZECTRIC = {
            "rulestring": "B3/S1234",
            "name": "Mazectric",
            "ruletime": 0 * TimeHelpers.SECOND.value
        }
        self.COAGULATIONS = {
            "rulestring": "B378/S235678",
            "name": "Coagulations",
            "ruletime": 0 * TimeHelpers.SECOND.value
        }
        self.BLINKERS = {
            "rulestring": "B3/S23",
            "name": "Blinkers",
            "ruletime": 10 * TimeHelpers.SECOND.value
        }

        self.collection = [self.CONWAY, self.HIGH_LIFE, self.DAY_NIGHT, self.MAZE, self.MAZECTRIC, self.COAGULATIONS, self.BLINKERS]

    def __getitem__(self, item: str):
        return [x for x in self.__dict__.values() if type(x) is not list and x["name"] == item][0]

    def __iter__(self):
        return iter(self.__dict__)

class Config:
    def __init__(self):
        self.screen_width = 1280
        self.screen_height = 720
        self.screen_sz = (self.screen_width, self.screen_height)
        self.cell_size = 10
        self.cycle = True
        self.grid_width = self.screen_width // self.cell_size
        self.grid_height = self.screen_height // self.cell_size
        self.default_speed = 10
        self.high_speed = 120
        self.speed = self.default_speed
        self.spawn_percent = 10
        self.background = (0, 0, 0)
        self.rules = Rules()
        self.rulecycle = cycle(self.rules.collection)
        self.rule = self.rules["Blinkers"]

    def cycle_rule(self):
        self.rule = next(self.rulecycle)
        print(self.rule)

    #def random_rule(self):
    #    self.rule = choice(self.rules)

    def get_ruleset_time(self):
        runtime = self.rule["ruletime"]
        return runtime

    def set_rule(self, rule: str):
        self.rule = rule
