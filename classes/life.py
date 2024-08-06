import pygame
import config, structures, grid, gameobj, screen

from random import randint, choices

class Game:
    def __init__(self):
        self.config = config.Config()
        self.grid = grid.Grid(self.config)
        self.screen = screen.Screen(self.config)
        self.clock = pygame.time.Clock()
        self.running = True

