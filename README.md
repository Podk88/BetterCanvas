`BetterCanvas` is wrapper around `tkinter.Canvas` class.

When you add an items to `tkinter.Canvas` it returns an `int` that serves as a new item identifier. 

```python
import tkinter as tk

canvas = tk.Canvas()
item_id = canvas.create_line(0, 0, 200, 100)
```

When you want to update your item you must pass its identifier or tag to one of the `Canvas` methods.
```python
canvas.move(item_id, 100, 100)
```

Instead `BetterCanvas` returns an object. 
```python
import BetterCanvas as bc
canvas = bc.BetterCanvas()
line = canvas.create_line(0, 0, 200, 100)
```
You can invoke methods of this object instead of managing identifiers or tags.
```python
line.move(100, 100)
```