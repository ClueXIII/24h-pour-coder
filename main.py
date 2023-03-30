import sys, time, pygame
from bouton import bouton

pygame.init()


def clearScreen():
    screen.fill(0, 0, 0)


# generer la fenetre du jeux
pygame.display.set_caption("Jeux 24H")
screen = pygame.display.set_mode((1080, 720))

running = True
image = "Sweet_Button_red-black.png"

#Charger le jeux

btn1= bouton(image,200,200, "red")
btn2= bouton(image,500,500, "red")

btn_list = []
btn_list.append(btn1)
btn_list.append(btn2)

current_link = 0

while running:

    # Background RGB
    screen.fill((255, 255, 255))

    # Placer une image a des coordonées
    btn1.printButton(screen)
    btn2.printButton(screen)

    # screen.blit(image, (x,y))

    # Mise a jour de l'écran
    pygame.display.flip()


    # proceed events

    # Fermeture du jeux
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_position = pygame.mouse.get_pos()
            print(mouse_position)
            if event.button == 1:  # 1= clique gauche
                i = 0

                for btn in btn_list:
                    x = btn.rect.x
                    y = btn.rect.y
                    if btn.zone.collidepoint(mouse_position):
                        print("in")
                        if not btn.linked:
                            if current_link == 0:
                                current_link = btn_list[i]
                                btn.linked = True
                            else:
                                if btn.couleur == current_link.couleur:
                                    btn.drawLine(screen, current_link)
                                    btn.linked = True
                                    current_link = 0
                i += 1

