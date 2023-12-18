import pygame

class GameFont:
    """
    Classe permettant de gérer les polices d'écritures
    """

    def __init__(self, screen, font_path, font_size, font_color, background_color=(0, 0, 0)):
        """
        screen: Écran sur lequel on affiche le jeu (pygame.Display)
        font_path: Chemin où se situe le fichier de la police d'écriture (String)
        font_size: Taille de la police d'écriture (Int)
        font_color: Couleur de la police d'écriture (Tuple RGB)
        background_color: Couleur du fond du texte (optionel) (Tuple RGB)

        Classe permettant de gérer les polices d'écritures
        """

        self.screen = screen
        self.font_path = font_path
        self.font_color = font_color
        self.background_color = background_color

        self.font = pygame.font.Font(font_path, font_size)
    
    def display(self, text_value, position):
        """
        text_value: Texte que l'on souhaite afficher (String)
        position: Position du texte (Tuple Coordonnées)
        """
        
        text = self.font.render(str(text_value), True, self.font_color, self.background_color)

        self.screen.blit(text, position)