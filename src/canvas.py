from tkinter import Tk, BOTH, Canvas
from drawing_tools import Line

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

        self.canvas = Canvas(self.__root)
        self.canvas.pack()
        self.running = False
    
    def redraw(self):
        """Redraws the image."""
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        """Set running to True and trigger redraw."""
        self.running = True
        
        while self.running: 
            self.redraw()
    
    def close(self):
        """Set running to False."""
        self.running = False

    def draw_line(self, line: Line, fill_color: str = "black", will_width: int = 2):
        """Draw a line on the canvas."""
        line.draw()
