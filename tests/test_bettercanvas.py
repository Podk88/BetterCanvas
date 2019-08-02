"""Tests for bettercanvas module."""
import pytest
import BetterCanvas as bc

class ItemWithoutCreateOnCanvasMethod(bc.Item):
    """MockItem class, that remembers args and kwargs."""

    def __init__(self, canvas, id, *args, **kwargs):
        super().__init__(canvas, id)

class TestBetterCanvas():
    def test_create_item_without_create_method(self, test_canvas):
        """Creating item without a create_on_canvas method should raise TypeError."""

        with pytest.raises(TypeError):
            test_canvas.create_item(ItemWithoutCreateOnCanvasMethod)

    



