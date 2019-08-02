"""Tests for the items module."""
import pytest

import BetterCanvas as bc


class TestItem():
    """Tests for the Item class."""

    def test_create_with_null_canvas(self):
        """Creating items with null canvas should raise a TypeError."""
        with pytest.raises(TypeError):
            bc.Item(id=1, canvas=None)

    def test_init(self, test_canvas):
        """Tests Item.__init__() assigns id and canvas attributes correctly."""
        item_id = 1
        item = bc.Item(id = item_id, canvas = test_canvas,)
        assert item.canvas == test_canvas
        assert item.id == item_id

class TestRectangle(TestItem):
    """Tests for Rectangle class."""
    
    @pytest.fixture(params=[(0, 0, 100), (0, 0, 100, 100, 100)], ids=['not enough', 'too much'])
    def invalid_rectangle_bbox(self, request):
        """Returns invalid rectangle bbox parameters."""
        return request.param

    def test_create_rectangle_with_invalid_bbox(self, test_canvas, invalid_rectangle_bbox):
        """Creating rectangle without exactly 4 nonkeyword parameters should raises a TypeError."""
        with pytest.raises(TypeError):
            bc.Rectangle.create_on_canvas(test_canvas, invalid_rectangle_bbox)

    def test_create_on_canvas(self, test_canvas):
        """Creating a rectangle should return a bc.Rectangle instance."""
        rectangle = bc.Rectangle.create_on_canvas(test_canvas, 0, 0, 100, 100)
        assert type(rectangle) == bc.Rectangle

    def test_create_rectangle_item(self, test_canvas):
        rectangle = test_canvas.create_item(bc.Rectangle, 0, 0, 100, 100)
        assert type(rectangle) == bc.Rectangle
