class Player:
    """
    This the player class where all associated attributes and methods are.
    """

    def __init__(self, canvas, start_pos, width, height, color, speed):
        """
        canvas: The canvas where the player need to be added (Canvas)
        start_pos: The position of player when the game start (Tuple)
        width: The width of the player (Integer)
        height: The height of the player (Integer)
        color: The color of the player (String)
        speed: The player's movement speed (Integer)
        """

        self.canvas = canvas
        self.start_pos = start_pos
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
    
        self.player_canva_object = canvas.create_rectangle(self.start_pos[0], self.start_pos[1], self.start_pos[0] + self.width, self.start_pos[1] + self.height, fill=self.color, outline='white')

    def up(self, event):
        self.canvas.move(self.player_canva_object, 0, -self.speed)

    def down(self, event):
        self.canvas.move(self.player_canva_object, 0, self.speed)