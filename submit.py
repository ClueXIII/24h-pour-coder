import pygame, time
import math


class submit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.width = 200
        self.height = 60
        self.image = pygame.image.load("submit.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.zone = pygame.Rect(self.rect.x - (self.width / 2), self.rect.y - (self.height / 2), self.width,
                                self.height)

    def printButton (self, screen):
        screen.blit(self.image, (self.rect.x-(self.width/2), self.rect.y-(self.height/2))) #changer taille en fonction

    def verifWin (self, btn_list):

        linked_number = 0
        for bouton in btn_list:
            if bouton.linked:
                linked_number += 1
            if linked_number >= len(btn_list) - 2:
                return True
        return False
