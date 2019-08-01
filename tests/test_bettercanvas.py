"""Tests for bettercanvas module."""
import pytest
import BetterCanvas as bc

class MockItem(bc.items.Item):
    """MockItem class, that remembers args and kwargs."""

    def __init__(self, canvas, *args, **kwargs):
        super().__init__(canvas)

        self.args = list(args)
        self.kwargs = kwargs

def test_item(better_canvas_instance ):
    """Tests creating items from BetterCanvas instance."""
    mock_item_class = MockItem
    args = [i for i in range(10)]
    kwargs = {str(i) : i*i for i in range(10)}
    item = better_canvas_instance.create_item(mock_item_class, *args, **kwargs)
    assert item.canvas == better_canvas_instance
    assert item.args == args
    assert item.kwargs == kwargs
