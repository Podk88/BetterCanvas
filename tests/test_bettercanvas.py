"""Tests for bettercanvas module."""
import pytest
import BetterCanvas as bc

class TestBetterCanvas():

    def test_create_rectangle(self, better_canvas):
        """create_rectangle method should return bc.Rectangle object."""
        rectangle = better_canvas.create_rectangle(0, 0, 100, 100)
        assert type(rectangle) == bc.Rectangle
        assert better_canvas.type(rectangle.id) == 'rectangle'

    def test_create_arc(self, better_canvas):
        """create_arc should return bc.Arc object."""
        arc = better_canvas.create_arc(0, 0, 100, 100)
        assert type(arc) == bc.Arc
        assert better_canvas.type(arc.id) == 'arc'

    bbox = [0, 0, 100, 100]
    position = [100, 100]
    values = [
        (bc.Rectangle, bbox),
        (bc.Arc, bbox),
        (bc.Bitmap, position),
        (bc.Image, position)
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


