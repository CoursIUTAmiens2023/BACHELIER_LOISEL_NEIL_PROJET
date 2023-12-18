from entities import player
from entities import ball
import pygame

pygame.init()

clock = pygame.time.Clock()

screen_width, screen_height = 1280, 720

fps = 30

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong Game")

in_game = True

p1 = player.Player(screen, x=0, y=screen_height/2, width=25, height=100, color=(0, 0, 255), speed=10)
p2 = player.Player(screen, x=screen_width-25, y=screen_height/2, width=25, height=100, color=(255, 0, 0), speed=10)
ball = ball.Ball(screen, x=screen_width/2-25, y=screen_height/2-25, width=25, height=25, color=(255,255,255), speed=10)

while in_game:
    screen.fill((0, 0, 0))
    ball.move()

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
    ball.show()
    ball.collision(p1,p2)

    pygame.display.flip()

    clock.tick(fps)