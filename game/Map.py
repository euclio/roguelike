from Tile import *

DEFAULT_GRID_SIZE = {'x': 256, 'y': 256}

class Map:
  def __init__(self, grid = None):
    if grid is None:
      self.grid = self.make_empty_grid(DEFAULT_GRID_SIZE['x'],
                                       DEFAULT_GRID_SIZE['y'])
    else:
      self.grid = grid

  def __getitem__(self, index):
    return self.grid[index]

  def __setitem__(self, index, tile):
    self.grid[index] = tile

  def get_grid_size(self):
    # Hack, assumes grid is square
    return {'x': len(self.grid),
            'y': len(self.grid[0])}

  def make_empty_grid(self, x, y):
    grid = [[Tile(BLANK_TILE_TYPE)] * x, [Tile(BLANK_TILE_TYPE)] * y]
    return grid

  def get_tile_at(self, x, y):
    return self.grid[x][y]
