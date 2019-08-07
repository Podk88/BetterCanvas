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

    def create_image(self, *position, **options) -> items.Bitmap:
        return self.create_item(items.Image, *position, **options)

    def create_item(self, item_type, *args, **kwargs) -> items.Item:
        """Returns new item of the given type.

        Args:
            item_type: type of the item that will be created.
        """
        return item_type(self.canvas, *args, **kwargs)