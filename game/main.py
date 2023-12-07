from entities import player
import pygame

pygame.init()

width, height = 1280, 720

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")

in_game = True

x, y = 10, 10

p1 = player.Player(screen, (1, 1), 5, 2, (0, 255, 0), 50)

while in_game:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            in_game = False

        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_UP):
                print("up")
                x += 1
            if (event.key == pygame.K_DOWN):
                print("down")
                x -= 1
    
    p1.show_player()
    
    pygame.display.flip()