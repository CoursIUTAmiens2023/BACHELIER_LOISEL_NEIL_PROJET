import pygame

class Player:
    """
    Classe représentant un joueur.
    """

    def __init__(self, screen, x, y, width, height, color, speed):
        """
        screen: Écran sur lequel on affiche le jeu (pygame.Display)
        x: Position horizontale du joueur (Un Entier ou un Float)
        y: Position verticale du joueur (Un Entier ou un Float)
        width: Largeur du joueur (Un Entier ou un Float)
        height: Hauteur du joueur (Un Entier ou un Float)
        color: couleur du joueur (Tuple RGB)
        speed: Vitesse du joueur (Un Entier)

        Classe représentant un joueur.
        """
        
        self.screen = screen
        self.color = color
        self.speed = speed
        self.rect = pygame.Rect(x, y, width, height)
    
    def move_up(self):
        """
        Méthode pour faire bouger le joueur vers le haut.
        """

        if (self.rect.top > 0):
            self.rect.move_ip(0, -self.speed)

    def move_down(self):
        """
        Méthode pour faire bouger le joueur vers le bas.
        """

        if (self.rect.bottom < self.screen.get_height()):
            self.rect.move_ip(0, self.speed)

    def show(self):
        """
        Méthode pour afficher le joueur.
        """
        
        pygame.draw.rect(self.screen, self.color, self.rect)