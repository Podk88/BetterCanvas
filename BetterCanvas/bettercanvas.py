"""This is a wrapper for tk.Canvas class."""

import tkinter as tk
from . import items

class BetterCanvas():
    """Wrapper for tk.Canvas."""

    def __init__(self, master=None, **kw):
        """Create a BetterCanvas widget with parent master."""
        self.canvas = tk.Canvas(master=master, **kw)
        self.items = {}
        super().__init__()

    def __getattr__(self, name):
        """Forward attribute look up to inner instance."""
        if hasattr(self.canvas, name):
            return getattr(self.canvas, name)
        else:
            raise AttributeError(f"{self} has no attribute {name}")

    def create_rectangle(self, *bbox, **options) -> items.Rectangle:
        return self.create_item(items.Rectangle, *bbox, **options)

    def create_arc(self, *bbox, **options) -> items.Arc:
        return self.create_item(items.Arc, *bbox, **options)

    def create_bitmap(self, *position, **options) -> items.Bitmap:
        return self.create_item(items.Bitmap, *position, **options)

    def create_image(self, *position, **options) -> items.Image:
        return self.create_item(items.Image, *position, **options)

    def create_line(self, *coords, **options) -> items.Line:
        return self.create_item(items.Line, *coords, **options)  
    
    def create_oval(self, *bbox, **options) -> items.Oval:
        return self.create_item(items.Oval, *bbox, **options)  

    def create_polygon(self, *coords, **options) -> items.Polygon:
        return self.create_item(items.Polygon, *coords, **options)

    def create_text(self, *position, **options) -> items.Text:
        return self.create_item(items.Text, *position, **options)
    
    def create_window(self, *position, **options) -> items.Window:
        return self.create_item(items.Window, *position, **options)        

    def create_item(self, item_type, *args, **kwargs) -> items.Item:
        """Returns new item of the given type.

        Args:
            item_type: type of the item that will be created.
        """
        item = item_type(self.canvas, *args, **kwargs)
        self.items[item.id] = item
        return item

    def find_above(item):
        """Returns the item just above the given item.

        Args:
            item: Reference item. """
        raise NotImplementedError

    def find_below(item):
        """Returns the item just below the given item.

        Args:
            item: Reference item. """
        raise NotImplementedError

    def find_closest(self, x, y, halo=None, start=None):

        """Returns the item closest to the given position. 
        
        Position is given in canvas coordinates. 
        Always succeeds if there’s at least one item in the canvas. 
        To find items within a certain distance from a position, 
        use find_overlapping with a small rectangle centered on the position.

        Args:
            x: Horizontal screen coordinate.
            y: Vertical screen coordinate.
            halo: Optional halo distance.
            start: Optional start item.
        Returns:
            Item instance. """
        raise NotImplementedError
    
    def find_enclosed(self, x1, y1, x2, y2):
        """Finds all items completely enclosed by the rectangle (x1, y1, x2, y2).

        Args:
            x1: Left edge.
            y1: Upper edge.
            x2: Right edge.
            y2: Lower edge.
        Returns:
            A tuple containing all matching items. """
        raise NotImplementedError
    
    
    def find_overlapping(self, x1, y1, x2, y2):
        """Finds all items that overlap the given rectangle, or that are completely enclosed by it.

        Args:
            x1: Left edge.
            y1: Upper edge.
            x2: Right edge.
            y2: Lower edge.
        Returns:
            A tuple containing all matching items. """
        raise NotImplementedError

    
    def find_withtag(self, tag):
        """Finds all items having the given tag."""
        raise NotImplementedError

    def focus(self):
        """Returns the item that currently has focus."""
        raise NotImplementedError

    