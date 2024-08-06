from enum import Enum


class Rules(Enum):
    CONWAY = "B2/S23"
    HIGH_LIFE = "B23/S36"
    DAY_NIGHT = "B3678/S34678"
    MAZE = "B3/S12345"
    MAZECTRIC = "B3/S1234"
    COAGULATIONS = "B378/S235678"
    ANTILIFE = "B0123478/S01234678"


class Config:
    def __init__(self):
        self.screen_width = 1280
        self.screen_height = 720
        self.screen_sz = (self.screen_width, self.screen_height)
        self.cell_size = 10
        self.grid_width = self.screen_width // self.cell_size
        self.grid_height = self.screen_height // self.cell_size
        self.default_speed = 30
        self.speed = self.default_speed
        self.background = (0, 0, 0)
        self.rule = Rules.CONWAY.value
