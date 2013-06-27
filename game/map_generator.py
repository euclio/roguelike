from __future__ import print_function
from map import Map
from tile import *
import random

def printTile(tile):
  if tile == FLOOR_TILE_TYPE:
     print('.', end='')
  elif tile == WALL_TILE_TYPE:
     print('#', end='')
  else:
    raise Exception("unknown tile type " +  str(tile.type_name))

def tileExistsInRectangle(map, y_start, x_start, height, width, tile):
  print(y_start, x_start, height, width)
  for y in range(y_start, y_start + height):
     for x in range(x_start, x_start + width):
       if map[y][x] == tile:
         return True
  return False

def floodFill(map, regionNumbersByTileCoord, startRow, startCol):
  tile = map[startRow][startCol]
  regionNumber = regionNumbersByTileCoord[(startRow, startCol)]
  
  for _ in range(0, max(map.get_grid_size()[0], map.get_grid_size()[1])):
    numModifies = 0
    
    for row in range(0, map.get_grid_size()[0]):
      for col in range(0, map.get_grid_size()[1]):
        if map[row][col] == tile:
          adjacent = False
          if row > 0:
            if map[row - 1][col] == tile:
              adjacent = True
          if row < map.get_grid_size()[0] - 1:
            if map[row + 1][col] == tile:
              adjacent = True
          if col > 0:
            if map[row][col - 1] == tile:
              adjacent = True
          if col < map.get_grid_size()[1] - 1:
            if map[row][col + 1] == tile:
              adjacent = True
          if adjacent:
            regionNumbersByTileCoord[(row, col)] = regionNumber
            numModifies += 1
    
    if numModifies == 0:
      break;

def generate_map():
  map = Map()
  num_rows, num_cols = map.get_grid_size()
  
  num_rooms = (num_cols * num_rows / 100 + random.randint(2, 5)) * 10
  
  for y in range(0, num_rows):
     for x in range(0, num_cols):
       map[y][x] = WALL_TILE_TYPE
  
  for _ in range(num_rooms):
    width = random.randint(6, 8)
    height = random.randint(4, 6)
    
    row = 1 + random.randint(0, num_rows - height - 2)
    col = 1 + random.randint(0, num_cols - width - 2)
    
    if not(tileExistsInRectangle(map, row - 1, col - 1, height + 2, width + 2, FLOOR_TILE_TYPE)):
      for y in range(row, row + height):
        for x in range(col, col + width):
          map[y][x] = FLOOR_TILE_TYPE
  
  regionNumbersByTileCoord = { }
  
  for y in range(0, num_rows):
     for x in range(0, num_cols):
       regionNumbersByTileCoord[(y, x)] = 0 # zero means it has no regionNumber
  
  for y in range(0, num_rows):
     for x in range(0, num_cols):
       if map[y][x] == FLOOR_TILE_TYPE and regionNumbersByTileCoord[(y, x)] == 0:
         floodFill(map, regionNumbersByTileCoord, y, x)
  
  for y in range(0, num_rows):
     for x in range(0, num_cols):
       print(chr(ord('A') + regionNumbersByTileCoord[(y, x)]), end='')
     print('', end='\n')
  
  
  # Random row, col
  # random width, height
  # place rooms, make sure they don't overlap
  # connect disconnected rooms
