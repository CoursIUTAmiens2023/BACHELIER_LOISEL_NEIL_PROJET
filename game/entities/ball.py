import pygame
import random

class Ball:
    def __init__(self, screen, x, y, width, height, color, speed):
        self.screen = screen
        self.color = color
        self.speed = speed
        direction = [-1, 1]
        self.movement_x = self.speed * random.choice(direction)
        self.movement_y = self.speed * random.choice(direction)
        self.rect = pygame.Rect(x, y, width, height)

    def move(self):
        if self.rect.top < 0:
            self.change_direction(change_x_direction=False, change_y_direction=True)
        elif self.screen.get_height() < self.rect.bottom:
            self.change_direction(change_x_direction=False, change_y_direction=True)

        self.rect.move_ip(self.movement_x, self.movement_y)
    
    def change_direction(self, change_x_direction=False, change_y_direction=False):
        if change_x_direction:
            self.movement_x = self.movement_x * -1
        elif change_y_direction:
            self.movement_y = self.movement_y * -1

    def show(self):
        """
        Méthode pour afficher le joueur
        """
        
        pygame.draw.ellipse(self.screen, self.color, self.rect)