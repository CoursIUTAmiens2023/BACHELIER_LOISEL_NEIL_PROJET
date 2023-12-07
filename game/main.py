from entities import player
import pygame

pygame.init()

width, height = 1280, 720

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")

in_game = True

p1 = player.Player(screen, x=0, y=height/2, width=25, height=100, color=(0, 255, 0), speed=10)

p2 = player.Player(screen, x=width-25, y=height/2, width=25, height=100, color=(0, 255, 0), speed=10)

while in_game:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        key = pygame.key.get_pressed()

        # Pour quitter le jeu
        if (event.type == pygame.QUIT):
            in_game = False

        # Mouvement du joueur 1
        if (key[pygame.K_z]):
            p1.move_up()
        if (key[pygame.K_s]):
            p1.move_down()

        # Mouvement du joueur 2
        if (key[pygame.K_KP_8]):
            p2.move_up()
        if (key[pygame.K_KP_2]):
            p2.move_down()
            
            
    
    p1.show()

    p2.show()

    pygame.display.flip()