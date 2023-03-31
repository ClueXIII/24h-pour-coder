import pygame
import time

from bouton import bouton
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
#Lvl1
lvl1 = []
btn1= bouton("Sweet_Button_red-black.png",205,200, "red")
btn2= bouton("Sweet_Button_red-black.png",400,200, "red")
lvl1.append(btn1)
lvl1.append(btn2)

lvl2 = []
btn1= bouton("Sweet_Button_red-black.png",205,200, "red")
btn2= bouton("Sweet_Button_red-black.png",400,200, "red")
btn3 = bouton("synthwaves_buttton_purple-lpurple.png",350,100,"purple")
btn4 = bouton("synthwaves_buttton_purple-lpurple.png",300,500,"purple")
lvl2.append(btn1)
lvl2.append(btn2)
lvl2.append(btn3)
lvl2.append(btn4)

lvl3 = []
btn1= bouton("Sweet_Button_red-black.png",205,400, "red")
btn2= bouton("Sweet_Button_red-black.png",400,300, "red")
btn3= bouton("Sweet_Button_red-black.png",100,500, "red")
btn4= bouton("Sweet_Button_red-black.png",600,500, "red")
btn5 = bouton("synthwaves_buttton_purple-lpurple.png",350,100,"purple")
btn6 = bouton("synthwaves_buttton_purple-lpurple.png",300,500,"purple")
btn7 = bouton("synthwaves_buttton_purple-lpurple.png",700,400,"purple")
lvl3.append(btn1)
lvl3.append(btn2)
lvl3.append(btn3)
lvl3.append(btn4)
lvl3.append(btn5)
lvl3.append(btn6)
lvl3.append(btn7)

lvl4 = []
btn1= bouton("Sweet_Button_red-black.png",205,400, "red")
btn2= bouton("Sweet_Button_red-black.png",400,300, "red")
btn3= bouton("Sweet_Button_red-black.png",100,500, "red")
btn4= bouton("Sweet_Button_red-black.png",600,500, "red")
btn5 = bouton("synthwaves_buttton_purple-lpurple.png",500,100,"purple")
btn6 = bouton("synthwaves_buttton_purple-lpurple.png",300,500,"purple")
btn7 = bouton("synthwaves_buttton_purple-lpurple.png",700,400,"purple")
btn8 = bouton("bouton_jaune.png",50,400,"yellow")
btn9 = bouton("bouton_jaune.png",500,600,"yellow")
btn10 = bouton("bouton_jaune.png",400,400,"yellow")
lvl4.append(btn1)
lvl4.append(btn2)
lvl4.append(btn3)
lvl4.append(btn4)
lvl4.append(btn5)
lvl4.append(btn6)
lvl4.append(btn7)
lvl4.append(btn8)
lvl4.append(btn9)
lvl4.append(btn10)

lvl = 0

lvl_list = [lvl1, lvl2, lvl3, lvl4]

btn_list = lvl_list[lvl]

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

logo = pygame.image.load("LOGO2.png")
logo = pygame.transform.scale(logo,(260,150))

mainMenu = True

#musics
play = True
pygame.mixer.music.load("musics/jeu24hFinalMenu.ogg")

while mainMenu:

    if play:
        pygame.mixer.music.play(loops=-1)
        play = False

    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))
    screen.blit(logo, (420,400))
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

play = True
pygame.mixer.music.load("musics/jeu24hFinal.ogg")

while running:
    if play:
        pygame.mixer.music.play(loops=-1)
        play = False

    # Background RGB

    if compteur % 100 == 0:
        bgGame = pygame.image.load("fondGameImp.png")
        bgGame = pygame.transform.scale(bgGame, (1080, 720))
    if compteur % 2 == 1:
        bgGame = pygame.image.load("fondGame.jpg")
        bgGame = pygame.transform.scale(bgGame, (1080, 720))
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

    submitBtn.printButton(screen)

    #Actualise l'écran
    pygame.display.flip()

    time.perf_counter()

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
                        print(btn.linked)
                        if not btn.linked and temp_link == None:  # Si le bouton n'est pas liée
                            temp_link = btn
                        elif not btn.linked and temp_link != None and btn.couleur == temp_link.couleur and btn != temp_link:

                            link_list.append(link(btn, temp_link))
                            temp_link.linked = True
                            temp_link = None
                        else:
                            temp_link = None
                if submitBtn.zone.collidepoint(mouse_position):
                    if submitBtn.verifWin(btn_list):
                        lvl += 1
                        screen.blit(bgGame, (0, 0))
                        link_list = []
                        btn_list = lvl_list[lvl]
            if event.button == 3:#Click Droit
                for btn in btn_list:
                    if btn.zone.collidepoint(mouse_position):
                        for element in link_list:
                            if element.end == btn:
                                btn.linked = False
                                element.start.linked = False
                                link_list.remove(element)

    compteur -=1
    clock.tick(60)
