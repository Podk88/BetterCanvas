"""This module contains classes that represent canvas items.

Items can be created with BetterCanvas create_x methods or on their own."""

import tkinter as tk
from functools import wraps

def forward(method):
    """Forward method calls to the canvas instance and supply the correct item id."""
    @wraps(method)
    def forwarded(self, *args, **kwargs):
        return getattr(self.canvas, method.__name__)(self.id, *args, **kwargs)
    return forwarded

class Item():
    """Base class for all item classes.
    
    All non abstract subclasses must implement _get_new_id method."""

    config_options=[]



    def __init__(self, **items):
        """Creates an Item instance that belongs to canvas Canvas."""
        self.init_options(**items)
        super().__init__(**self.get_other_options(**items))

    @forward
    def move(self, dx, dy):
        """Moves canvas item by the provided offset."""

    def _get_new_id(self, *args, **options) -> int:
        """Creates a new item on self.canvas and returns its id."""
        raise NotImplementedError

    def init_options(self, **options):
        """Set the given options of the item.
        
        Args:
            options: {option : value}."""
        for option, value in options.items():
            self.__setattr__(option, value)

    @classmethod
    def get_create_options(cls, **options):
        """Returns only options relevant to the class."""
        return {option : value for option, value in options.items() if option in cls.config_options}

    @classmethod
    def get_other_options(cls, **options):
        """Return options not relevant to the current class."""
        return {option : value for option, value in options.items() if option not in cls.config_options}

    @property
    @forward
    def bbox(self):
        """The bounding box, as a 4-tuple.
        Note that the bounding box is approximate and may differ a few pixels from the real value.
        """ 

    @property
    @forward
    def coords(self):
        """Returns the coordinates of the item."""
    
    @coords.setter
    @forward
    def coords(self, *newcoords):
        """Sets the coordinates of the item."""

    @property
    def tags(self):
        """Returns all tags attached to the item."""
        return self.canvas.gettags(self.id)

    @tags.setter
    def tags(self, new_tags):
        """Replaces all tags attached to the item."""
        self.canvas.itemconfig(self.id, tags=new_tags)

    def __getattr__(self, name):
        """Return property of the item."""
        if name in self.config_options:
            return self.canvas.itemcget(self.id, name)
        raise AttributeError(f"{self} has no attribute {name}.")

    def __setattr__(self, name, value):
        if name in self.config_options:
            self.canvas.itemconfig(self.id, {name:value})
        else:
            super().__setattr__(name, value)

    @forward
    def delete(self):
        """Deletes the underlying item from the canvas."""

    @forward
    def focus(self):
        """Sets focus to this item."""

    def bind(self, event, callback, add=False):
        """Adds an event binding to the item.

        Args:
            event (str): Event descriptor.
            callback (callable): Callable to bind to the event.
            add (bool): Add new binding to any existing bindings or replace them, defaults to replace.
        """
        if add:
            add = "+"
        else:
            add = None
        self.canvas.tag_bind(self.id, event, callback, add)

class Rectangle(Item):
    """Rectangle canvas item."""

    def __init__(self, canvas: tk.Canvas, *bbox, **kwargs):
        if len(bbox) != 4:
            raise TypeError(f"Rectangle item expects 4 values as its bounding box. {len(bbox)} were given.")
        self.canvas = canvas
        self.id = self._get_new_id(*bbox)
        super().__init__(**kwargs)
        
    config_options = set([
        'activedash',
        'activefill',
        'activeoutline',
        'activeoutlinestipple',
        'activestipple',
        'activewidth',
        'dash',
        'dashoffset',
        'disableddash',
        'disabledfill',
        'disabledoutline',
        'disabledoutlinestipple',
        'disabledstipple',
        'disabledwidth',
        'fill',
        'offset',
        'outline',
        'outlineoffset',
        'outlinestipple',
        'state',
        'stipple',
        'tags',
        'width'
    ])

    def _get_new_id(self, *bbox, **options) -> int:
        """Creates a new id of rectangle item on self.canvas."""
        return self.canvas.create_rectangle(*bbox, **options)


class Arc(Item):
    """Arc canvas item."""

    config_options = set([
        'activedash',
        'activefill',
        'activeoutlin',
        'activeoutlinestipple',
        'activestipple',
        'activewidth',
        'dash',
        'dashoffset',
        'disableddash',
        'disabledfill',
        'disabledoutline',
        'disabledoutlinestipple',
        'disabledstipple',
        'disabledwidth',
        'extent',
        'fill',
        'offset',
        'outline',
        'outlineoffset',
        'outlinestipple',
        'start',
        'state',
        'stipple',
        'style',
        'tags',
        'width'
    ])

    def __init__(self, canvas: tk.Canvas, *bbox, **kwargs):
        if len(bbox) != 4:
            raise TypeError(f"Arc item expects 4 values as its bounding box. {len(bbox)} were given.")
        self.canvas = canvas
        self.id = self._get_new_id(*bbox)
        super().__init__(**kwargs)

    def _get_new_id(self, *bbox) -> int:
        """Creates a new id of arc item on self.canvas."""
        return self.canvas.create_arc(*bbox)

class Bitmap(Item):
    """Bitmap canvas item."""
    
    config_options = set([
        'activebackground',
        'activebitmap',
        'activeforeground',
        'anchor',
        'background',
        'bitmap',
        'disabledbackground',
        'disabledbitmap',
        'disabledforeground',
        'foreground',
        'state',
        'tags'
    ])

    def __init__(self, canvas: tk.Canvas, *position, **kwargs):
        if len(position) != 2:
            raise TypeError(f"Image item expects 2 values as its position box. {len(position)} were given.")
        self.canvas = canvas
        self.id = self._get_new_id(*position)
        super().__init__(**kwargs)

    def _get_new_id(self, *position) -> int:
        """Creates a bitmap item on self.canvas and returns its id."""
        return self.canvas.create_bitmap(*position)

class Image(Item):
    """Image canvas item."""
    
    config_options = set([
        'activeimage',
        'anchor',
        'disabledimage',
        'image',
        'state',
        'tags'
    ])

    def __init__(self, canvas: tk.Canvas, *position, **kwargs):
        if len(position) != 2:
            raise TypeError(f"Image item expects 2 values as its position. {len(position)} were given.")
        self.canvas = canvas
        self.id = self._get_new_id(*position)
        super().__init__(**kwargs)

    def _get_new_id(self, *position) -> int:
        """Creates a image item on self.canvas and returns its id."""
        return self.canvas.create_image(*position) 

class Line(Item):
    """Line canvas item."""
        
    config_options = set([
        'activedash',
        'activefill',
        'activestipple',
        'activewidth',
        'arrow',
        'arrowshape',
        'capstyle',
        'dash',
        'dashoffset',
        'disableddash',
        'disabledfill',
        'disabledstipple',
        'disabledwidth',
        'fill',
        'joinstyle',
        'offset',
        'smooth',
        'splinesteps',
        'state',
        'stipple',
        'tags',
        'width',
    ])

    def __init__(self, canvas: tk.Canvas, *coords, **kwargs):
        if len(coords) != 4:
            raise TypeError(f"Line item expects 4 values as its position. {len(coords)} were given.")
        self.canvas = canvas
        self.id = self._get_new_id(*coords)
        super().__init__(**kwargs)

    def _get_new_id(self, *coords) -> int:
        """Creates a line item on self.canvas and returns its id."""
        return self.canvas.create_line(*coords) 

class Oval(Item):
    """Oval canvas item."""
    
    config_options = set([
        'activedash',
        'activefill',
        'activeoutline',
        'activeoutlinestipple',
        'activestipple',
        'activewidth',
        'dash',
        'dashoffset',
        'disableddash',
        'disabledfill',
        'disabledoutline',
        'disabledoutlinestipple',
        'disabledstipple',
        'disabledwidth',
        'fill',
        'offset',
        'outline',
        'outlineoffset',
        'outlinestipple',
        'state',
        'stipple',
        'tags',
        'width',
    ])

    def __init__(self, canvas: tk.Canvas, *bbox, **kwargs):
        if len(bbox) != 4:
            raise TypeError(f"Oval item expects 4 values as its position. {len(bbox)} were given.")
        self.canvas = canvas
        self.id = self._get_new_id(*bbox)
        super().__init__(**kwargs)

    def _get_new_id(self, *bbox) -> int:
        """Creates an oval item on self.canvas and returns its id."""
        return self.canvas.create_oval(*bbox) 

class Polygon(Item):
    """Polygon canvas item."""
    
    config_options = set([
        'activedash',
        'activefill',
        'activeoutline',
        'activeoutlinestipple',
        'activestipple',
        'activewidth',
        'dash',
        'dashoffset',
        'disableddash',
        'disabledfill',
        'disabledoutline',
        'disabledoutlinestipple',
        'disabledstipple',
        'disabledwidth',
        'fill',
        'joinstyle',
        'offset',
        'outline',
        'outlineoffset',
        'outlinestipple',
        'smooth',
        'splinesteps',
        'state',
        'stipple',
        'tags',
        'width',
    ])

    def __init__(self, canvas: tk.Canvas, *coords, **kwargs):
        if len(coords) % 2 != 0:
            raise TypeError(f"Polygon item expects an even number of coordinates. {len(coords)} were given.")
        self.canvas = canvas
        self.id = self._get_new_id(*coords)
        super().__init__(**kwargs)

    def _get_new_id(self, *coords) -> int:
        """Creates an oval item on self.canvas and returns its id."""
        return self.canvas.create_polygon(*coords) 

class Text(Item):
    """Text canvas item."""
    
    config_options = set([
        'activefill',
        'activestipple',
        'anchor',
        'disabledfill',
        'disabledstipple',
        'fill',
        'font',
        'justify',
        'offset',
        'state',
        'stipple',
        'tags',
        'text',
        'width',
    ])

    def __init__(self, canvas: tk.Canvas, *position, **kwargs):
        if len(position) != 2:
            raise TypeError(f"Text item expects 2 arguments as its coordinates. {len(position)} were given.")
        self.canvas = canvas
        self.id = self._get_new_id(*position)
        super().__init__(**kwargs)

    def _get_new_id(self, *position) -> int:
        """Creates an text item on self.canvas and returns its id."""
        return self.canvas.create_text(*position) 

    @forward
    def dchars(self, start, to=None):
        """Deletes text.
        
        Args:
            start: Where to start deleting text.
            to: Where to stop deleting text. 
            If omitted, a single character is removed."""

    @forward
    def icursor(self, index):
        """Moves the insertion cursor to the given position."""
    
    @forward
    def index(self, index):
        """Gets the numerical cursor index corresponding to the given index. 
        
        Numerical indexes work like Python’s sequence indexes; 
        0 is just to the left of the first character, 
        and len(text) is just to the right of the last character.
        
        Args:
            index: An index. 
                You can use a numerical index, or one of the following:
                INSERT (the current insertion cursor), 
                END (the length of the text), 
                SEL_FIRST and SEL_LAST (the selection start and end). 
                “@x,y” where x and y are canvas coordinates, 
                to get the index closest to the given coordinate.
        Returns:
            A numerical index (an integer).
        """

    @forward
    def insert(self, index, text):
        """Inserts text into an item.
        
        Args:
            index: Where to insert the text. This can be either a numerical index or a symbolic constant. 
                See the description of the index method for details. 
                If you insert text at the INSERT index, the cursor is moved along with the text. 
            text: The text to insert.
        """

class Window(Item):
    """Window canvas item is used to place another widget on the canvas."""
    
    config_options = set([
        'anchor',
        'height',
        'state',
        'tags',
        'width',
        'window',
    ])

    def __init__(self, canvas: tk.Canvas, *position, **kwargs):
        if len(position) != 2:
            raise TypeError(f"Window item expects 2 arguments as its coordinates. {len(position)} were given.")
        self.canvas = canvas
        self.id = self._get_new_id(*position)
        super().__init__(**kwargs)

    def _get_new_id(self, *position) -> int:
        """Creates an text item on self.canvas and returns its id."""
        return self.canvas.create_window(*position) 