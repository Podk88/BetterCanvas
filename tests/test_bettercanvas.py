"""Tests for bettercanvas module."""
import pytest
import BetterCanvas as bc

class ItemWithoutCreateOnCanvasMethod(bc.Item):
    """MockItem class, that remembers args and kwargs."""

    def __init__(self, canvas, *args, **kwargs):
        super().__init__(canvas)

class TestBetterCanvas():

    item_types = [bc.Rectangle]

    @pytest.fixture(params=item_types, ids=[type.__name__ for type in item_types])
    def item_type(self, request):
        return request.param

    def test_create_rectangle(self, test_canvas):
        """create_rectangle method should return bc.Rectangle object."""
        rectangle = test_canvas.create_rectangle(0, 0, 100, 100)
        assert type(rectangle) == bc.Rectangle

    def test_create_item(self, test_canvas, item_type):
        """create_item method should return an object of the correct type."""
        new_item = test_canvas.create_item(item_type, 0, 0, 100, 100)
        assert type(new_item) == item_type



