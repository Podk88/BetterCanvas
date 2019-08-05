"""This module contains classes that represent canvas items.

Items can be created with BetterCanvas create_x methods or on their own."""

import tkinter as tk

class Item():
    """Base class for all item classes.
    
    All non abstract subclasses must implement _get_new_id method."""

    def __init__(self, canvas: tk.Canvas, **kwargs):
        """Creates an Item instance that belongs to canvas Canvas."""
        super().__init__(**kwargs)
        if canvas == None:
            raise TypeError("Parameter canvas must be not None.")
        self.canvas = canvas

    def move(self, dx, dy):
        """Moves canvas item by the provided offset."""
        self.canvas.move(self.id, dx, dy)

    def _get_new_id(self, *args, **options) -> int:
        """Creates a new item on self.canvas and returns its id."""
        raise NotImplementedError

class Rectangle(Item):
    """Rectangle canvas item."""

    def __init__(self, canvas: tk.Canvas, *bbox, **kwargs):
        if len(bbox) != 4:
            raise TypeError(f"Rectangle class expects 4 values as its bounding box. {len(bbox)} were given.")
        super().__init__(canvas, **kwargs)
        self.id = self._get_new_id(*bbox, **kwargs)

    def _get_new_id(self, *bbox, **options) -> int:
        """Creates a new id of rectangle item on self.canvas."""
        return self.canvas.create_rectangle(*bbox, **options)
    


