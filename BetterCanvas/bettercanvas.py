"""This is a wrapper for tk.Canvas class."""

import tkinter as tk
from . import items

class BetterCanvas(tk.Canvas):
    """Wrapper for tk.Canvas."""

    def __init__(self, master=None, **kw):
        """Create a BetterCanvas widget with parent master."""
        super().__init__(master=master, **kw)

    def create_item(self, item_type, *args, **kwargs):
        """Returns new item of the given type.

        Args:
            item_type: type of the item that will be created.
        Raises:
            TypeError: When item_type does not have a create_method property. 
        """
        if not hasattr(item_type, 'create_on_canvas'):
            raise TypeError(f"{item_type} has no attribute create_on_canvas.")
        return item_type.create_on_canvas(self, *args, **kwargs)