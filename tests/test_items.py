"""Tests for the items module."""
import pytest

import BetterCanvas as bc


class TestItem():
    """Tests for the Item class."""

    def test_init(self, better_canvas_instance):
        """Tests Item.__init__() method."""

        with pytest.raises(TypeError):
            bc.Item(None)

        item = bc.Item(better_canvas_instance)
        assert item.canvas == better_canvas_instance

class TestRectangle(TestItem):
    """Test for the Rectangle class."""
    
    @pytest.fixture(params=[(0, 0, 100), (0, 0, 100, 100, 100)], ids=['not enough', 'too much'])
    def invalid_rectangle_params(self, request):
        """Returns invalid rectangle bbox parameters."""
        return request.param

    def test_param_count(self, better_canvas_instance, invalid_rectangle_params):
        """Tests Rectangle creation with invalid number of parameters."""
        with pytest.raises(TypeError):
            bc.Rectangle(better_canvas_instance, *invalid_rectangle_params)

    def test_init(self, better_canvas_instance):
        """Tests Rectangle.__init__() method."""
        super().test_init(better_canvas_instance)

        rectangle = bc.Rectangle(better_canvas_instance, 0, 0, 100, 100)
        assert hasattr(rectangle, 'id')
