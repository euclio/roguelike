from tile import *

DEFAULT_GRID_SIZE = 256, 256

def make_empty_grid(y, x):
  grid = []
  for i in xrange(y):
    grid.append([Tile(BLANK_TILE_TYPE)] * x)
  return grid

class Map:
  def __init__(self, grid=None):
    if grid is None:
      x, y = DEFAULT_GRID_SIZE
      self.grid = make_empty_grid(x, y)
    else:
      self.grid = grid

  def __getitem__(self, index):
    return self.grid[index]

  def __setitem__(self, index, tile):
    self.grid[index] = tile

  def get_grid_size(self):
    return len(self.grid), len(self.grid[0])

  def get_tile_at(self, y, x):
    return self.grid[y][x]
