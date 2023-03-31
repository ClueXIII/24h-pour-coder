import pygame
import math


class impultion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Boule.png")
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y-90
        self.vect = []
        self.compte = 0

    '''
    def impultionMove(self, btn_start, btn_dest, speed, screen):
        x = btn_dest.rect.centerx
        y = btn_dest.rect.centery
        if not self.vect:
            d = ((self.rect.centerx-x) ** 2 + (self.rect.centery-y) ** 2) ** 0.5
            self.vect[0] = d/60
            self.vect[1] = d/60
            if self.rect.centerx > x :
    '''
    def impultionMove(self, btn_start, btn_dest, speed, screen):

        x = btn_dest.rect.centerx-40
        y = btn_dest.rect.centery-40
        d = ((self.rect.centerx - x) ** 2 + (self.rect.centery - y) ** 2) ** 0.5
        if d < 50:
            self.kill()
        elif not self.vect:
            self.vect = [int(x - (self.rect.centerx))/60, int(y - (self.rect.centery))/60]


            # self.rect.move(speed * vect[0], speed * vect[1])

        self.rect.centerx += speed * self.vect[0]
        self.rect.centery += speed * self.vect[1]

        self.compte += 1
