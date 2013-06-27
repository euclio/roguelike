from map import Map
import random

def generate_map():
  the_map = Map()
  num_rooms = random.randint(5, 20)
  max_x, max_y = the_map.get_grid_size()
  for _ in num_rooms:
    row = random.randint(0, max_x)
    col = random.randint(0, max_y)

  # Random row, col
  # random width, height
  # place rooms, make sure they don't overlap
  # connect disconnected rooms
