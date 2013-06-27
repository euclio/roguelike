#!/usr/bin/python
from system.rgame import *
from map import *

class World:
  def __init__(self):
    self.message = "default message"
    self.map = Map()

world = World()

def inputHandler(ch):
  world.message = ch

# Hand over control to C++ right away.
# world: A world object, containing all data structures
#   that C++ needs to render
# inputHandler: A function for reacting to the input from
#   a keypress
GameInit(world, inputHandler)
