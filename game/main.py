from entities import player
import pygame

pygame.init()

width, height = 1280, 720

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")

in_game = True

p1 = player.Player(screen, x=0, y=height/2, width=25, height=100, color=(0, 255, 0), speed=50)

p2 = player.Player(screen, x=width-25, y=height/2, width=25, height=100, color=(0, 255, 0), speed=50)

while in_game:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            in_game = False

        if (event.type == pygame.KEYDOWN):
            # Mouvement du joueur 1
            if (event.key == pygame.K_UP):
                p1.move_up()
            if (event.key == pygame.K_DOWN):
                p1.move_down()
            
            # Mouvement du joueur 2
            if (event.key == 122):
                p2.move_up()
            if (event.key == 115):
                p2.move_down()
    
    p1.show()
    
    p2.show()

    pygame.display.flip()