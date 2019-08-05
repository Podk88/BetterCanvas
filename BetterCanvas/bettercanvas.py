"""This is a wrapper for tk.Canvas class."""

import tkinter as tk
from . import items

class BetterCanvas():
    """Wrapper for tk.Canvas."""

    def __init__(self, master=None, **kw):
        """Create a BetterCanvas widget with parent master."""
        self.canvas = tk.Canvas(master=master, **kw)
        super().__init__()

    def __getattr__(self, name):
        """Forward attribute look up to inner instance."""
        if name in vars(self.canvas):
            return getattr(self.canvas, name)
        else:
            raise AttributeError(f"{self} has no attribute {name}")

    def create_rectangle(self, *bbox, **options) -> items.Rectangle:
        return self.create_item(items.Rectangle, *bbox, **options)

    def create_item(self, item_type, *args, **kwargs):
        """Returns new item of the given type.

        Args:
            item_type: type of the item that will be created.
        """
        return item_type(self.canvas, *args, **kwargs)