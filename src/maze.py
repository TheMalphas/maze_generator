import time
from graphics import Window, Point, Cell

class Maze:
    """Maze."""

    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        """Maze constructor."""
        self._cells: list[list[Cell]] = []

        self._x1: int = x1
        self._y1: int = y1
        self._num_rows: int = num_rows
        self._num_cols: int = num_cols
        self._cell_size_x: int = cell_size_x
        self._cell_size_y: int = cell_size_y
        self._win: Window = win

        self._create_cells()
    
    def _create_cells(self):
        """Calculate position of cells."""
        
        for _ in range(self._num_cols):
            cell_col = []
            for _ in range(self._num_rows):
                cell_col.append(Cell(self._win))
            self._cells.append(cell_col)
        
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        """Draw cells after calculation."""
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        """Visualizes the working algorithms."""
        self._win.redraw()
        time.sleep(0.01)
