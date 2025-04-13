from dataclasses import dataclass

from tkinter import Canvas

@dataclass
class Point:
    """Store public data members."""

    def __init__(cls, x: int = 0, y: int = 0):
        """Point constructor."""
        cls.x = x
        cls.y = y


class Line:
    """Draw line."""

    def __init__(self, start: Point, end: Point):
        """Line constructor."""
        self.start = start
        self.end = end
    
    def draw(self, canvas: Canvas, fill_color: str = "black", fill_width: int = 2):
        """Draw a line."""
        canvas.create_line(
            self.start.x, self.start.y,
            self.end.x, self.end.y,
            fill=fill_color,
            width=fill_width
        )
