import tkinter as tk

import pytest

import BetterCanvas as bc


@pytest.fixture
def better_canvas_instance():
    """BetterCanvas instance used in other tests."""
    return bc.BetterCanvas()
