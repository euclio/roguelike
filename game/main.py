#!/usr/bin/python
from system.rgame import *
from map import *
from input import handle_input, PlayerAction
from gameplay import handle_gameplay, game_state

def input_handler(ch):
  action = handle_input(ch)
  handle_gameplay(action)

# Hand over control to C++ right away.
# world: A world object, containing all data structures
#   that C++ needs to render
# inputHandler: A function for reacting to the input from
#   a keypress
GameInit(game_state, input_handler)
