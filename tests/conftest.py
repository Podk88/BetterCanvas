import tkinter as tk

import pytest

import BetterCanvas as bc


@pytest.fixture
def test_canvas():
    """BetterCanvas instance used in other tests."""
    return bc.BetterCanvas()
