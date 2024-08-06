from random import randint, choices
from enum import Enum


class GameObjectShape(Enum):
    SQUARE = 0
    CIRCLE = 1
    TRIANGLE = 2


class Colors(Enum):
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)


class PastelColors(Enum):
    PINK = (255, 105, 180)
    LIGHT_BLUE = (173, 216, 230)
    LIGHT_GREEN = (144, 238, 144)
    LIGHT_YELLOW = (255, 255, 224)
    LIGHT_PURPLE = (221, 160, 221)
    LIGHT_ORANGE = (255, 160, 122)
    LIGHT_BROWN = (210, 105, 30)
    LIGHT_GRAY = (211, 211, 211)
    LIGHT_PINK = (255, 182, 193)
    LIGHT_CYAN = (224, 255, 255)
    LIGHT_MAGENTA = (255, 192, 203)

class GameObject:
    def __init__(self, location: tuple, color=None, z_index=0):
        self.location = location
        self.color = color if color else self.random_pastel_color()
        self.z_index = z_index if z_index else 0
        self.render = True

    def set_location(self, location: tuple) -> tuple:
        self.location = location
        return self.location

    def set_color(self, color: tuple) -> None:
        self.color = color

    def randomize_color(self) -> None:
        self.color = self.random_pastel_color()

    @staticmethod
    def random_pastel_color() -> tuple:
        return choices(list(PastelColors))[0].value

    @staticmethod
    def random_saturated_color() -> tuple:
        return choices(list(Colors))[0].value

    @staticmethod
    def random_color() -> tuple:
        return randint(0, 255), randint(0, 255), randint(0, 255)
