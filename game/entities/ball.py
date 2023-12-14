import pygame
import random

class Ball:
    """
    Classe représentant une balle.
    """

    def __init__(self, screen, x, y, width, height, color, speed):
        """
        screen: Écran sur lequel on affiche le jeu (pygame.Display)
        x: Position horizontale de la balle (Un Entier ou un Float)
        y: Position verticale de la balle (Un Entier ou un Float)
        width: Largeur de la balle (Un Entier ou un Float)
        height: Hauteur de la balle (Un Entier ou un Float)
        color: Couleur de la balle (Tuple RGB)
        speed: Vitesse de la balle (Un Entier)

        Classe représentant une balle.
        """
        self.screen = screen
        self.color = color
        self.speed = speed
        direction = [-1, 1]
        self.movement_x = self.speed * random.choice(direction)
        self.movement_y = self.speed * random.choice(direction)
        self.rect = pygame.Rect(x, y, width, height)

    def move(self):
        """
        Méthode pour faire bouger la balle.
        """
        if self.rect.top < 0:
            self.change_direction(change_x_direction=False, change_y_direction=True)
        elif self.screen.get_height() < self.rect.bottom:
            self.change_direction(change_x_direction=False, change_y_direction=True)

        self.rect.move_ip(self.movement_x, self.movement_y)
    
    def change_direction(self, change_x_direction=False, change_y_direction=False):
        """
        change_x_direction: Variable (optionel) indiquant de changer la direction horizontale de la balle (Booléen)
        change_y_direction: Variable (optionel) indiquant de changer la direction verticale de la balle (Booléen)

        Méthode pour changer la direction de la balle.
        """
        if change_x_direction:
            self.movement_x = self.movement_x * -1
        elif change_y_direction:
            self.movement_y = self.movement_y * -1

    def show(self):
        """
        Méthode pour afficher la balle.
        """
        
        pygame.draw.ellipse(self.screen, self.color, self.rect)