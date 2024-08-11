from enum import Enum
from random import choice


class Rules(Enum):
    CONWAY = "B3/S23"
    HIGH_LIFE = "B23/S36"
    DAY_NIGHT = "B3678/S34678"
    MAZE = "B3/S12345"
    MAZECTRIC = "B3/S1234"
    COAGULATIONS = "B378/S235678"
    ANTILIFE = "B0123478/S01234678"
    BLINKERS = "B3/S23"

class TimeHelpers(Enum):
    SECOND = 1000
    MINUTE = 1000 * 60
    HOUR = 60 * 60 * 1000
    DAY = 24 * 60 * 60 * 1000

class RuleOrder:
    def __init__(self):
        self.rules = list(Rules)
        self.index = 0

    def current_rule(self):
        return self.rules[self.index]

    def next_rule(self):
        self.index += 1
        if self.index >= len(self.rules):
            self.index = 0

    def previous_rule(self):
        self.index -= 1
        if self.index < 0:
            self.index = len(self.rules) - 1

    def peek_next_rule(self):
        return self.rules[self.index + 1]

    def peek_previous_rule(self):
        return self.rules[self.index - 1]

    def current_rule(self):
        return self.rules[self.index]

class Config:
    def __init__(self):
        self.screen_width = 1280
        self.screen_height = 720
        self.screen_sz = (self.screen_width, self.screen_height)
        self.cell_size = 10
        self.grid_width = self.screen_width // self.cell_size
        self.grid_height = self.screen_height // self.cell_size
        self.default_speed = 3
        self.high_speed = 120
        self.speed = self.default_speed
        self.spawn_percent = 10
        self.background = (0, 0, 0)
        self.rule = Rules.ANTILIFE
        self.rule_order = RuleOrder()
        self.ruleset_times = {
            Rules.CONWAY: 5 * TimeHelpers.SECOND.value,
            Rules.HIGH_LIFE: 5 * TimeHelpers.SECOND.value,
            Rules.DAY_NIGHT: 5 * TimeHelpers.SECOND.value,
            Rules.MAZE: 5 * TimeHelpers.SECOND.value,
            Rules.MAZECTRIC: 5 * TimeHelpers.SECOND.value,
            Rules.COAGULATIONS: 5 * TimeHelpers.SECOND.value,
            Rules.ANTILIFE: 5 * TimeHelpers.SECOND.value,
            Rules.BLINKERS: 5 * TimeHelpers.SECOND.value
            }

    def random_rule(self):
        self.rule = choice(list(Rules))

    def get_ruleset_time(self):
        runtime = self.ruleset_times.get(self.rule)
        return runtime

    def set_rule(self, rule: str):
        self.rule = rule

    def set_rule_from_rule_order(self):
        self.rule = self.rule_order.current_rule()

    def get_rule_string(self):
        rule_strings = {
            Rules.CONWAY: "Conway's Game of Life",
            Rules.HIGH_LIFE: "High Life",
            Rules.DAY_NIGHT: "Day/Night",
            Rules.MAZE: "Maze",
            Rules.MAZECTRIC: "Mazectric",
            Rules.COAGULATIONS: "Coagulations",
            Rules.ANTILIFE: "AntiLife",
            Rules.BLINKERS: "Blinkers"
        }
        return rule_strings[self.rule]
