from tkinter import Tk, BOTH, Canvas
from dataclasses import dataclass


def CenterWindowToDisplay(Screen: Tk, width: int, height:int):
    """Center the window to the main display/monitor."""

    screen_width = Screen.winfo_screenwidth()
    screen_height = Screen.winfo_screenheight()
    x = int((screen_width/2) - width/2)
    y = int((screen_height/2) - height/2)
    return f"{width}x{height}+{x}+{y}"

class Window:
    """Window to draw."""

    def __init__(self, width: int, height: int):
        """Screen constructor."""

        self.__root = Tk()
        self.__root.geometry(CenterWindowToDisplay(self.__root, width, height))
        self.__root.title = "Maze"
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.__canvas = Canvas(self.__root, bg="white")
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
    
    def redraw(self):
        """Redraws the image."""
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        """Set running to True and trigger redraw."""
        self.__running = True
        while self.__running: 
            self.redraw()
    
    def draw_line(self, line: 'Line', fill_color: str = "black", fill_width: int = 2):
        """Draw a line on the canvas."""
        line.draw(self.__canvas, fill_color, fill_width)

    def close(self):
        """Set running to False."""
        self.__running = False



@dataclass
class Point:
    """Store public data members."""

    x: int = 0
    y: int = 0


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