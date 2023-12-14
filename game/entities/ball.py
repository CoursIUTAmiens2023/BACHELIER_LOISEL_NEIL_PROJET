import pygame
import random

class Ball:
    def __init__(self, screen, x, y, width, height, color,speed):
        self.screen = screen
        self.color = color
        self.speed = speed
        self.rect = pygame.Rect(x,y,width,height)

    def move(self):
        movements = [-self.speed,self.speed]
        if(self.rect.top > 0 and self.rect.bottom < self.screen.get_height()):
            self.rect.move_ip(random.choice(movements),self.speed)

    def show(self):
        """
        Méthode pour afficher le joueur
        """
        
        pygame.draw.ellipse(self.screen, self.color, self.rect)

