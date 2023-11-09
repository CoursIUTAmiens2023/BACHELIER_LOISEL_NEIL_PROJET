from entities import player
from tkinter import *

# Creation of the window
window = Tk()
window.title('Pong Game')
width, height = 1280, 720

# Creation of the canvas
# The canvas is where we render all the game elements
canvas = Canvas(window, width=width, height=height)
canvas.pack(fill='both', expand=True)

# Creation of the player 1
p1_width = 10
p1_height = 100
p1_start_pos = (0, 0)
p1_color = 'blue'
p1_speed = 10
p1 = player.Player(canvas, p1_start_pos, p1_width, p1_height, p1_color, p1_speed)
canvas.bind_all('<z>', p1.up)
canvas.bind_all('<s>', p1.down)

# Creation of the player 2
p2_width = 10
p2_height = 100
p2_start_pos = (width - p2_width, height - p2_height)
p2_color = 'red'
p2_speed = 10
p2 = player.Player(canvas, p2_start_pos, p2_width, p2_height, p2_color, p2_speed)
canvas.bind_all('<Up>', p2.up)
canvas.bind_all('<Down>', p2.down)

window.mainloop()