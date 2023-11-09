from tkinter import *

# Creation of the window
window = Tk()
window.title('Pong Game')
width, height = 1280, 720

# Creation of the canvas
# The canvas is where we render all the game elements
canvas = Canvas(window, width=width, height=height)
canvas.pack(fill='both', expand=True)

paddle = canvas.create_rectangle(0, 0, 30, 150, fill='blue', outline='white')

def haut(event):
    canvas.move(paddle, 0, -10)

def bas(event):
    canvas.move(paddle, 0, 10)

canvas.bind_all('<Up>', haut)
canvas.bind_all('<Down>', bas)

window.mainloop()