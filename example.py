import tkinter as tk

import BetterCanvas as bc

root = tk.Tk()
canvas = bc.BetterCanvas(root)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
canvas.grid(sticky="NSEW")

size = (200, 300)

rectangle = canvas.create_rectangle(0, 0, 100, 100)
rectangle.move(100, 100)

root.mainloop()
