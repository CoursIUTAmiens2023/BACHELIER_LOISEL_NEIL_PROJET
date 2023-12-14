import pygame
import random

class Ball:
    def __init__(self, screen, x, y, width, height, color, speed):
        direction = [-1, 1]

        self.screen = screen
        self.color = color
        self.speed = speed
        self.direction_x = self.speed * random.choice(direction)
        self.direction_y = self.speed * random.choice(direction)
        self.rect = pygame.Rect(x, y, width, height)

    def move(self):
        if self.rect.top < 0:
            self.change_direction(direction_y=1)
        elif self.screen.get_height() < self.rect.bottom:
            self.change_direction(direction_y=-1)

        self.rect.move_ip(self.speed * self.direction_x, self.speed * self.direction_y)
    
    def change_direction(self, direction_x=1, direction_y=1):
        self.direction_x = direction_x
        self.direction_y = direction_y

    def show(self):
        """
        Méthode pour afficher le joueur
        """
        
        pygame.draw.ellipse(self.screen, self.color, self.rect)