from canvas import Window
from drawing_tools import Point, Line

def main():
    """Main."""
    win = Window(800, 600)
    canvas = win.canvas
    start, end = Point(50, 50), Point(100, 100)
    line = Line(start, end)
    line.draw(canvas)
    win.wait_for_close()









if __name__ == "__main__":
    main()