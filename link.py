import pygame
from impultion import *


class link(pygame.sprite.Sprite):
    def __init__(self, end, start):
        super().__init__()
        self.end = end
        self.start = start
        self.all_impultion = pygame.sprite.Group()

    def launch_impultion(self):
        self.all_impultion.add(impultion(self.start.rect.centerx-40, self.start.rect.centery+40))

