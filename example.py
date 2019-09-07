import tkinter as tk

import BetterCanvas as bc

root = tk.Tk()
canvas = bc.BetterCanvas(root)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
canvas.grid(sticky="NSEW")

size = (200, 300)

rectangle = canvas.create_item(bc.Rectangle, 0, 0, 100, 100)
rectangle.move(200, 100)

text = canvas.create_text(200, 200, text="Hello world!")
text.insert(0, "WUB!")
text.dchars(5,8)

root.mainloop()
