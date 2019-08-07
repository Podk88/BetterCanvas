import tkinter as tk

import pytest

import BetterCanvas as bc


@pytest.fixture
def better_canvas():
    """BetterCanvas instance used in other tests."""
    return bc.BetterCanvas()

@pytest.fixture
def tk_canvas():
    return tk.Canvas()
