import numpy as np

class Environment:
    def __init__(self, grid_size):
        """
        Initialize the environment with a grid of zeros.
        :param grid_size: Tuple (rows, cols) defining the grid dimensions.
        """
        self.grid_size = grid_size
        self.grid = np.zeros(grid_size, dtype=int)

    def add_obstacle(self, x, y):
        """
        Mark a cell as an obstacle.
        :param x: Row index.
        :param y: Column index.
        """
        if 0 <= x < self.grid_size[0] and 0 <= y < self.grid_size[1]:
            self.grid[x][y] = 1

    def remove_obstacle(self, x, y):
        """
        Remove an obstacle from a cell.
        :param x: Row index.
        :param y: Column index.
        """
        if 0 <= x < self.grid_size[0] and 0 <= y < self.grid_size[1]:
            self.grid[x][y] = 0
