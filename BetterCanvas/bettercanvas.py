"""This is a wrapper for tk.Canvas class."""

import tkinter as tk
from . import items

class BetterCanvas(tk.Canvas):
    """Wrapper for tk.Canvas."""

    def __init__(self, master=None, **kw):
        """Create a BetterCanvas widget with parent master."""
        super().__init__(master=master, **kw)

    def rectangle(self, *bbox, **options):
        """Returns new Rectangle item with given bounds and options."""
        return self.create_item(items.Rectangle, *bbox, **options) 

    def create_item(self, item_factory, *args, **kwargs):
        """Returns new item produced by item_factory.

        Args:
            item_factory: callable that returns new item instance. 
            Will be called as item_factory(self, *args, **kwargs)."""
        return item_factory(self, *args, **kwargs)