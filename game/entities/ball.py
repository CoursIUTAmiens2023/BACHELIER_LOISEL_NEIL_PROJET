import pygame

class Ball:
    def __init__(self, screen, x, y, width, height, color,speed):
        self.screen = screen
        self.color = color
        self.speed = speed
        self.rect = pygame.Rect(x,y,width,height)

    def show(self):
        """
        Méthode pour afficher le joueur
        """
        
        pygame.draw.ellipse(self.screen, self.color, self.rect)

