import pygame
import random

class Ball:
    """
    Classe représentant une balle.
    """

    def __init__(self, screen, x, y, width, height, color, speed):
        """
        screen: Écran sur lequel on affiche le jeu (pygame.Display)
        x: Position horizontale de la balle (Int ou Float)
        y: Position verticale de la balle (Int ou Float)
        width: Largeur de la balle (Int ou Float)
        height: Hauteur de la balle (Int ou Float)
        color: Couleur de la balle (Tuple RGB)
        speed: Vitesse de la balle (Int)

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
            self.change_direction(change_x_direction=False, change_y_direction=True, player=None)
        elif self.screen.get_height() < self.rect.bottom:
            self.change_direction(change_x_direction=False, change_y_direction=True, player=None)

        self.rect.move_ip(self.movement_x, self.movement_y)
    
    def change_direction(self, change_x_direction=False, change_y_direction=False, player=None):
        """
        change_x_direction: Variable (optionel) indiquant de changer la direction horizontale de la balle (Bool)
        change_y_direction: Variable (optionel) indiquant de changer la direction verticale de la balle (Bool)
        player: Joueur avec lequel la balle intéragit avec (player.Player)

        Méthode pour changer la direction de la balle.
        """

        if change_x_direction:
            self.movement_x = self.movement_x * -1
        elif change_y_direction:
            self.movement_y = self.movement_y * -1

        if player is not None:
            offset = self.rect.centery - player.rect.centery
            self.movement_y += offset / 10  

    def show(self):
        """
        Méthode pour afficher la balle.
        """
        
        pygame.draw.ellipse(self.screen, self.color, self.rect)
    
    def collision(self, player1, player2):
        """
        player1: Joueur 1 (player.Player)
        player2: Joueur 2 (player.Player)
        
        Méthode qui gère la collision entre les joueurs et la balle.
        """
        
        if(self.rect.colliderect(player1.rect)):
            self.change_direction(change_x_direction=True, change_y_direction=True, player=player1)
        elif(self.rect.colliderect(player2.rect)):
            self.change_direction(change_x_direction=True, change_y_direction=True, player=player2)
    
    def change_position(self,x,y,width,height):
        self.rect.update(x,y,width,height)
    
    def reset_movement(self):
        direction = [-1, 1]
        self.movement_x = self.speed * random.choice(direction)
        self.movement_y = self.speed * random.choice(direction)
