import pygame

pygame.init()

width, height = 1280, 720

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")

in_game = True

while in_game:
    pygame.display.update()