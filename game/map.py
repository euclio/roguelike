from tile import *

DEFAULT_GRID_SIZE = 256, 256

class Map:
  def __init__(self, grid=None):
    if grid is None:
      x, y = DEFAULT_GRID_SIZE
      self.grid = self.make_empty_grid(x, y)
    else:
      self.grid = grid

  def __getitem__(self, index):
    return self.grid[index]

  def __setitem__(self, index, tile):
    self.grid[index] = tile

  def get_grid_size(self):
    # Hack, assumes grid is rectangular
    return len(self.grid), len(self.grid[0])

  def make_empty_grid(self, x, y):
    for col in range(x):
      for row in range(y):
        grid[row][col] = BLANK_TILE_TYPE
    return grid

  def get_tile_at(self, x, y):
    return self.grid[x][y]
