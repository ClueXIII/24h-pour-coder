import pygame

class bouton(pygame.sprite.Sprite):
    def __init__(self,image,x,y, couleur):
        super().__init__()
        self.width = self.height = 80
        self.image = pygame.transform.scale(pygame.image.load(image), (int(self.width), int(self.height)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.zone = pygame.Rect(self.rect.x-(self.width/2), self.rect.y-(self.height/2), self.width, self.height)
        self.linked = False
        self.couleur = couleur

    def printButton (self, screen):
        screen.blit(self.image, (self.rect.x-(self.width/2), self.rect.y-(self.height/2))) #changer taille en fonction

    def drawLine (self, screen, btn2):
        pygame.draw.line(screen, "black", (self.rect.x, self.rect.y), (btn2.rect.y, btn2.rect.y))
        self.printButton(screen)
        btn2.printButton(screen)


