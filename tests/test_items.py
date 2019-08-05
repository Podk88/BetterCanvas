"""Tests for the items module."""
import pytest

import BetterCanvas as bc


class TestItem():
    """Tests for the Item class."""

    def test_create_with_null_canvas(self):
        """Creating items with null canvas should raise a TypeError."""
        with pytest.raises(TypeError):
            bc.Item(canvas=None)

    def test_init(self, test_canvas):
        """Tests Item.__init__() assigns canvas attribute correctly."""
        item = bc.Item(canvas = test_canvas)
        assert item.canvas == test_canvas

class TestRectangle(TestItem):
    """Tests for Rectangle class."""
    
    @pytest.fixture(params=[(0, 0, 100), (0, 0, 100, 100, 100)], ids=['not enough', 'too much'])
    def invalid_rectangle_bbox(self, request):
        """Returns invalid rectangle bbox parameters."""
        return request.param

    def test_create_rectangle_with_invalid_bbox(self, test_canvas, invalid_rectangle_bbox):
        """Creating rectangle without exactly 4 nonkeyword parameters should raises a TypeError."""
        with pytest.raises(TypeError):
            bc.Rectangle(test_canvas, invalid_rectangle_bbox)

    # def test_create_on_canvas(self, test_canvas):
    #     """Creating a rectangle should return a bc.Rectangle instance."""
    #     rectangle = test_canvas.create_item(bc.Rectangle, 0, 0, 100, 100)
    #     assert type(rectangle) == bc.Rectangle


