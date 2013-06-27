class TileType:
  def __init__(self):
    self.type_name = "invalid"

  def __init__(self, type_name):
    self.type_name = type_name.lower()

FLOOR_TILE_TYPE = TileType("floor")
DOOR_TILE_TYPE = TileType("door")
WALL_TILE_TYPE = TileType("wall")
WATER_TILE_TYPE = TileType("water")
LAVA_TILE_TYPE = TileType("lava")
BLANK_TILE_TYPE = TileType("blank")
INVALID_TILE_TYPE = TileType("invalid")

class Tile:
  def __init__(self, tile_type = None):
    self.tile_type = tile_type
