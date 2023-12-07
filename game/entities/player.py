import pygame

class Player:
    """
    This the player class where all associated attributes and methods are.
    """

    def __init__(self, screen, pos, width, height, color, speed):
        """
        window: 
        pos: The position of player when the game start (Tuple)
        width: The width of the player (Integer)
        height: The height of the player (Integer)
        color: The color of the player (String)
        speed: The player's movement speed (Integer)
        """

        self.screen = screen
        self.pos = pos
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
        # self.rect = pygame.Rect(pos[0] - width/2, pos[1] - height/2, pos[0] + width/2, pos[1] + height/2)
        self.rect = pygame.Rect(0, 0, 0 + width/2, 0 + height/2)
    
    def show_player(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    # def up(self, event):
    #     self.rect.move(self.player_canva_object, 0, -self.speed)

    # def down(self, event):
    #     self.rect.move(self.player_canva_object, 0, self.speed)