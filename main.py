import sys, time, pygame
from bouton import bouton
from impultion import impultion
from link import link
from submit import submit
from play import play

pygame.init()
clock = pygame.time.Clock()


def clearScreen():
    screen.fill(0, 0, 0)


# generer la fenetre du jeux
pygame.display.set_caption("Jeux 24H")
screen = pygame.display.set_mode((1080, 720))

running = True
image = "Sweet_Button_red-black.png"

#Charger le jeux


btn1= bouton(image,100,55, "red")
btn2= bouton(image,115,250, "red")
btn3= bouton(image,500,410, "red")
btn4= bouton(image,400,25, "red")


btn_list = []
btn_list.append(btn1)
btn_list.append(btn2)
btn_list.append(btn3)
btn_list.append(btn4)

link_list = []

compteur = 60

temp_link = None

submitBtn = submit(540,650)

playBtn = play(540, 300)

#le fond
bg = pygame.image.load("fond.png")
bg = pygame.transform.scale(bg,(1080,720))

bgGame = pygame.image.load("fondGame.jpg")
bgGame = pygame.transform.scale(bgGame,(1080,720))

mainMenu = True

while mainMenu:

    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))
    playBtn.printButton(screen)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if event.button == 1:#Click Gauche

                    if playBtn.zone.collidepoint(mouse_position):
                        mainMenu = False

while running:
    # Background RGB
    screen.fill((0, 0, 0))
    screen.blit(bgGame, (0, 0))

    #Creation de toutes les instances de link
    for linked in link_list:
        for impultion in linked.all_impultion:
            impultion.impultionMove(linked.start,linked.end,1,screen)
        linked.all_impultion.draw(screen)

    #Affichage des Boutton
    for btn in btn_list:
        btn.printButton(screen)

    if compteur == 0:
        for linked in link_list:
            linked.launch_impultion()
        compteur = 60

    #submitBtn.printButton(screen)

    #Actualise l'écran
    pygame.display.flip()

    # Fermeture du jeux
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        #Gestion du reliage
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            if event.button == 1:  # Click Gauche
                for btn in btn_list:
                    if btn.zone.collidepoint(mouse_position):
                        if not btn.linked and temp_link == None:  # Si le bouton n'est pas liée
                            temp_link = btn
                        elif not btn.linked and temp_link != None and btn.couleur == temp_link.couleur:
                            link_list.append(link(btn, temp_link))
                            linked_number = 0
                            for bouton in btn_list:
                                if bouton.linked:
                                    linked_number += 1
                                if linked_number == len(btn_list)-2:
                                    print("lvl terminé")
                            temp_link.linked = True
                            temp_link = None
                        else:
                            temp_link = None
                if submitBtn.zone.collidepoint(mouse_position):
                    if submitBtn.verifWin(btn_list):
                        print("lvl terminé")
            if event.button == 3:#Click Droit
                for btn in btn_list:
                    if btn.zone.collidepoint(mouse_position):
                        print(btn.linked)
                        for element in link_list:
                            if element.end == btn:
                                btn.linked = False
                                element.start.linked = False
                                link_list.remove(element)

    compteur -=1
    clock.tick(60)
