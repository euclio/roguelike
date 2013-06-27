from tile import *
from map import *

class Level:
  def __init__(self, map_ = None, entity_grid = None):
    self.map_ = map_
    self.entity_grid = entity_grid

  def get_entities_at(self, x, y):
    return self.entity_grid[x][y]
