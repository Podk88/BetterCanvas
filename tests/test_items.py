"""Tests for the items module."""
import pytest

import BetterCanvas as bc

class MockItem(bc.Item):

    def __init__(self, canvas, **kwargs):
        self.canvas = canvas
        options = self.get_create_options(**kwargs)
        self.id = self._get_new_id(0, 0, 100, 100, **options)
        return super().__init__(**kwargs)

    def _get_new_id(self, *bbox, **options):
        return self.canvas.create_rectangle(*bbox, **options)


@pytest.fixture
def mock_item(tk_canvas):
    return MockItem(tk_canvas)

def test_coords(mock_item):
    assert mock_item.coords == [0, 0, 100, 100]
    new_coords = [100, 100, 200, 200]
    mock_item.coords = new_coords
    assert mock_item.coords == new_coords

class TestItemConfig():

    def test_unknown_option(self, mock_item):
        """Accessing an option outside of config_option should rise an error."""
        with pytest.raises(AttributeError):
            mock_item.not_an_option



class TestTags():
    """Tests for tags assignment, deletion, etc."""

    @pytest.fixture(params=[("one", ), ("two", "FOO")], ids = ["single tag", "multiple tags"])
    def tags(self, request):
        return request.param

    @pytest.fixture
    def mock_item(self, test_canvas):
        return MockItem(test_canvas.canvas)

    def test_init_w_tags(self, tk_canvas, tags):
        item = bc.Rectangle(tk_canvas, 0, 0, 100, 100, tags=tags)
        assert item.tags == tags
        for tag in tags:
            assert tk_canvas.find_withtag(tag) == (item.id, )

    def test_set_no_tags(self, tk_canvas, tags):
        item = bc.Rectangle(tk_canvas, 0, 0, 100, 100, tags=tags)

        item.tags = ()
        assert item.tags == ()
        for tag in tags:
            assert tk_canvas.find_withtag(tag) == ()

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
        assert better_canvas.type(rectangle.id) == 'rectangle'


class TestArc():
    """Tests for Arc class."""

    def test_create_with_create_item(self, better_canvas):
        """Creating an arc should return a bc.Arc instance."""
        arc = better_canvas.create_item(bc.Arc, 0, 0, 100, 100)
        assert type(arc) == bc.Arc

class TestBitmap():
    """Tests for Bitmap class."""

    def test_create_with_create_item(self, better_canvas):
        """Creating a bitmap should return a bc.Bitmap instance."""
        bitmap = better_canvas.create_item(bc.Bitmap, 0, 0)
        assert type(bitmap) == bc.Bitmap

class TestImage():
    """Tests for Image class."""

    def test_create_with_create_item(self, better_canvas):
        """Creating an image should return a bc.Image instance."""
        image = better_canvas.create_item(bc.Image, 0, 0)
        assert type(image) == bc.Image

class TestLine():
    """Tests for Line class."""

    def test_create_with_create_item(self, better_canvas):
        """Creating a line should return a bc.Line instance."""
        image = better_canvas.create_item(bc.Line, 0, 0, 100, 100)
        assert type(image) == bc.Line

class TestPolygon():
    """Tests for Polygon class."""

    def test_create_with_create_item(self, better_canvas):
        """Creating a polygon should return a bc.Polygon instance."""
        image = better_canvas.create_item(bc.Polygon, 0, 0, 100, 100)
        assert type(image) == bc.Polygon




