from tkinter import Canvas
from graphics import Point, Line, Window


class Cell:
    """Cell self-drawing class."""

    def __init__(self, win: Window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win: Window = win

    @property
    def get_center_point(self):
        if any([self._x1, self._x2, self._y1, self._y2]) == None:
            raise 'Cell is missing coordinates.'
        half_length = abs(self._x2 - self._x1) // 2
        x_center = half_length + self._x1
        y_center = half_length + self._y1

        return Point(x_center, y_center)

    def draw(self, x1, y1, x2, y2, broken=False):
        """Draw method."""
        if self._win is None:
            return

        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        top_left_corner = Point(x1, y1)
        bottom_left_corner = Point(x1, y2)
        top_right_corner = Point(x2, y1)
        bottom_right_corner = Point(x2, y2)

        def inner_draw(corners):

            line = Line(corners[0], corners[1])

            if broken:
                self._win.draw_line(line, "white")
            else:  
                self._win.draw_line(line)

        inner_draw((top_left_corner, bottom_left_corner))
        inner_draw((top_left_corner, top_right_corner))
        inner_draw((top_right_corner, bottom_right_corner))
        inner_draw((bottom_left_corner, bottom_right_corner))

    def draw_move(self, to_cell: 'Cell', undo=False):
        """Draw a line between two cells."""

        start = self.get_center_point
        end = to_cell.get_center_point

        fill_color = "red"
        if undo:
            fill_color = "gray"

        line = Line(start, end)
        self._win.draw_line(line, fill_color)
