"""This module contains classes that represent canvas items.

Items can be created with BetterCanvas create_x methods or on their own."""

import tkinter as tk

class Item():
    """Base class for all item classes."""

    def __init__(self, canvas: tk.Canvas, **kwargs):
        """Create an Item instance that belongs to canvas Canvas."""
        super().__init__(**kwargs)
        if canvas == None:
            raise TypeError("Parameter canvas must be not None.")
        self.canvas = canvas

    def move(self, dx, dy):
        """Moves canvas item by the provided offset."""
        self.canvas.move(self.id, dx, dy)

class Rectangle(Item):
    """Rectangle canvas item."""

    def __init__(self, canvas: tk.Canvas, *bbox, **kwargs):
        super().__init__(canvas, **kwargs)

        if len(bbox) != 4:
            raise TypeError(f"Rectangle class expects 4 values as its bounding box. {len(bbox)} were given.")

        self.id = canvas.create_rectangle(*bbox, **kwargs)
