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

    def verifWin (self, screen, liste_btn):
        for btn in liste_btn:
            print(btn.linked)
            if btn.linked is False :
                return False
        print("niquel")

        return True
