"""Tests for bettercanvas module."""
import pytest
import BetterCanvas as bc

class TestBetterCanvas():

    bbox = [0, 0, 100, 100]
    position = [100, 100]
    coords = [50, 50, 100, 100]
    values = [
        (bc.Rectangle, bbox),
        (bc.Arc, bbox),
        (bc.Bitmap, position),
        (bc.Image, position),
        (bc.Line, coords),
        (bc.Oval, bbox),
        (bc.Polygon, coords),
        (bc.Text, position),
        (bc.Window, position)
    ]

    @pytest.mark.parametrize('item_type, args', values)
    def test_create_item(self, better_canvas, item_type, args):
        """create_item method should return an object of the correct type."""
        new_item = better_canvas.create_item(item_type, *args)
        assert type(new_item) == item_type
        assert better_canvas.type(new_item.id) == item_type.__name__.lower()

    @pytest.mark.parametrize('item_type, args', values)
    def test_create_x_method(self, better_canvas, item_type, args):
        """create_item method should return an object of the correct type."""
        new_item = getattr(better_canvas, f'create_{item_type.__name__.lower()}')(*args)
        assert type(new_item) == item_type
        assert better_canvas.type(new_item.id) == item_type.__name__.lower()


