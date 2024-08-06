import pygame


class Screen:
    def __init__(self, config):
        self.config = config
        self.surface = pygame.display.set_mode(self.config.screen_sz)

    def draw(self, gameobjs: list):
        self.surface.fill(self.config.background)
        new_gameobjs = sorted(filter(lambda x: x.render, gameobjs), key=lambda x: x.z_index)
        for gameobj in new_gameobjs:
            if gameobj.render:
                pygame.draw.rect(self.surface,
                                 gameobj.color,
                                 gameobj.location +
                                 (self.config.cell_size, self.config.cell_size)
                                 )
        pygame.display.flip()
