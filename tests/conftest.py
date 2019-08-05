import tkinter as tk

import pytest

import BetterCanvas as bc


item_types = [bc.Rectangle]

@pytest.fixture(params=item_types, ids=[type.__name__ for type in item_types])
def item_type(request):
    return request.param

@pytest.fixture
def better_canvas():
    """BetterCanvas instance used in other tests."""
    return bc.BetterCanvas()

@pytest.fixture
def tk_canvas():
    return tk.Canvas()
