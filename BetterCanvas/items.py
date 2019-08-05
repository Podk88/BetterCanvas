"""This module contains classes that represent canvas items.

Items can be created with BetterCanvas create_x methods or on their own."""

import tkinter as tk

class Item():
    """Base class for all item classes.
    
    All non abstract subclasses must implement _get_new_id method."""

    def __init__(self, **kwargs):
        """Creates an Item instance that belongs to canvas Canvas."""
        
        self.tags = kwargs.pop("tags", ())

        super().__init__(**kwargs)

    def move(self, dx, dy):
        """Moves canvas item by the provided offset."""
        self.canvas.move(self.id, dx, dy)

    def _get_new_id(self, *args, **options) -> int:
        """Creates a new item on self.canvas and returns its id."""
        raise NotImplementedError

    @property
    def bbox(self):
        return self.canvas.bbox(self.id)

    @property
    def coords(self):
        """Returns the coordinates of the item."""
        return self.canvas.coords(self.id)
    
    @coords.setter
    def coords(self, *newcoords):
        """Sets the coordinates of the item."""
        self.canvas.coords(self.id, *newcoords)

    @property
    def tags(self):
        """Returns all tags attached to the item."""
        return self.canvas.gettags(self.id)

    @tags.setter
    def tags(self, new_tags):
        """Replaces all tags attached to the item."""
        self.canvas.itemconfig(self.id, tags=new_tags)
class Rectangle(Item):
    """Rectangle canvas item."""

    def __init__(self, canvas: tk.Canvas, *bbox, **kwargs):
        if len(bbox) != 4:
            raise TypeError(f"Rectangle class expects 4 values as its bounding box. {len(bbox)} were given.")
        self.canvas = canvas
        self.id = self._get_new_id(*bbox, **kwargs)
        super().__init__(**kwargs)
        

    def _get_new_id(self, *bbox, **options) -> int:
        """Creates a new id of rectangle item on self.canvas."""
        return self.canvas.create_rectangle(*bbox, **options)
    


