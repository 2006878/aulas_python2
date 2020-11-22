from tkinter import Tk, Canvas
from typing import NewType
root = Tk
def begin(event):
    global oldx, oldy
    oldx, oldy = event.x, event.y

def draw(event):
     global oldx, oldy, canvas
     newx, newy = event.x, event.y
     canvas.create_line(oldx, oldy, newx, newy)
     oldx, oldy = newx, newy   
oldx, oldy =0, 0
canvas = Canvas(root, height=100, width=150)
canvas.bind("<Button-1>", draw)
canvas.pack()
root.mainloop