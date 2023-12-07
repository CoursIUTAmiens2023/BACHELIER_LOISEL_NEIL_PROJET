import pygame

class Player:
    """
    Classe du joueur.
    """

    def __init__(self, screen, x, y, width, height, color, speed):
        """
        screen: Écran sur lequel on affiche le jeu (pygame.Display)
        x: Position horizantale du joueur (Un Entier ou un Float)
        y: Position verticale du joueur (Un Entier ou un Float)
        width: La largeur du joueur (Un Entier ou un Float)
        height: La hauteur du joueur (Un Entier ou un Float)
        color: La couleur du joueur (String)
        speed: La vitesse du joueur (Un Entier ou un Float)
        """

        self.screen = screen
        self.color = color
        self.speed = speed
        self.rect = pygame.Rect(x, y, width, height)
    
    def move_up(self):
        """
        Méthode pour faire bouger le joueur vers le haut
        """

        self.rect.move_ip(0, -self.speed)

    def move_down(self):
        """
        Méthode pour faire bouger le joueur vers le bas
        """

        self.rect.move_ip(0, self.speed)

    def show(self):
        """
        Méthode pour afficher le joueur
        """
        
        pygame.draw.rect(self.screen, self.color, self.rect)