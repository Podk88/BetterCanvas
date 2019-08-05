"""Tests for the items module."""
import pytest

import BetterCanvas as bc

class MockItem(bc.Item):

    def __init__(self, canvas, **kwargs):
        self.canvas = canvas
        self.id = self._get_new_id(0, 0, 100, 100)
        return super().__init__(**kwargs)

    def _get_new_id(self, *bbox, **options):
        return self.canvas.create_rectangle(*bbox, **options)


@pytest.fixture
def mock_item(tk_canvas):
    return MockItem(tk_canvas)






class TestRectangle():
    """Tests for Rectangle class."""
    
    @pytest.fixture(params=[(0, 0, 100), (0, 0, 100, 100, 100)], ids=['not enough', 'too much'])
    def invalid_rectangle_bbox(self, request):
        """Returns invalid rectangle bbox parameters."""
        return request.param

    def test_create_rectangle_with_invalid_bbox(self, tk_canvas, invalid_rectangle_bbox):
        """Creating rectangle without exactly 4 nonkeyword parameters should raises a TypeError."""
        with pytest.raises(TypeError):
            bc.Rectangle(tk_canvas, invalid_rectangle_bbox)

    def test_create_with_create_item(self, better_canvas):
        """Creating a rectangle should return a bc.Rectangle instance."""
        rectangle = better_canvas.create_item(bc.Rectangle, 0, 0, 100, 100)
        assert type(rectangle) == bc.Rectangle


