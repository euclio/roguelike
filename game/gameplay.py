from map import make_empty_grid, Map
from player import PlayerEntity

class Actions:
  UP_ACTION = 1
  DOWN_ACTION = 2
  LEFT_ACTION = 3
  RIGHT_ACTION = 4
  INTERACT = 5
  ABILITY = 6
  INVENTORY = 7
  CANCEL = 8
  NO_ACTION = 9

_DEFAULT_KEYBINDINGS = {
    'w': Actions.UP_ACTION,
    '8': Actions.UP_ACTION,
    'a': Actions.LEFT_ACTION,
    '4': Actions.LEFT_ACTION,
    's': Actions.DOWN_ACTION,
    '2': Actions.DOWN_ACTION,
    'd': Actions.RIGHT_ACTION,
    '6': Actions.RIGHT_ACTION,
    'e': Actions.INTERACT,
    'f': Actions.ABILITY,
    'q': Actions.INVENTORY,
}

keybindings = _DEFAULT_KEYBINDINGS

def handle_input(input_key):
    return keybindings.get(input_key, PlayerAction.NO_ACTION)

class GameState(object):
  def __init__(self):
    self.tile_map = Map(make_empty_grid(25, 25))
    self.player = PlayerEntity((10,10))

def handle_gameplay(key):
  if game_state.player.is_on_map():
    action = keybindings.get(key, Actions.NO_ACTION)
    _do_map_action(action)
  else:
    _do_inventory_action(key)

def _do_inventory_action(key):
  pass

def _do_map_action(action):
  if action == Actions.UP_ACTION:
    game_state.player.move_up()
  elif action == Actions.LEFT_ACTION:
    game_state.player.move_left()
  elif action == Actions.DOWN_ACTION:
    game_state.player.move_down()
  elif action == Actions.RIGHT_ACTION:
    game_state.player.move_right()
  elif action == Actions.INTERACT:
    game_state.player.interact()
  elif action == Actions.ABILITY:
    game_state.player.use_ability()
  elif action == Actions.INVENTORY:
    game_state.player.enter_inventory()
  elif action == Actions.NO_ACTION:
    pass
  else:
    raise ValueError('Invalid player action encountered')

game_state = GameState()
