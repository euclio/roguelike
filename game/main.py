#!/usr/bin/python
from system.rgame import *
from map import *
from input import handle_input, PlayerAction
from gameplay import handle_gameplay

class World:
  def __init__(self):
    self.message = "default message"
    self.map = Map(make_empty_grid(10, 10))
    self.pointer = (1, 1)

world = World()

def input_handler(ch):
  action = handle_input(ch)
  handle_gameplay(world, action)

# Hand over control to C++ right away.
# world: A world object, containing all data structures
#   that C++ needs to render
# inputHandler: A function for reacting to the input from
#   a keypress
GameInit(world, input_handler)
