from map import make_empty_grid, Map
class Player:
  def __init__(self):
    self.location = (10, 10)

class GameState(object):
  def __init__(self):
    self.tile_map = Map(make_empty_grid(25, 25))
    self.player = Player()

def handle_gameplay(action):
  if action == PlayerAction.MOVE_UP:
    pass
  elif action == PlayerAction.MOVE_UP:
    pass
  elif action == PlayerAction.MOVE_LEFT:
    pass
  elif action == PlayerAction.MOVE_DOWN:
    pass
  elif action == PlayerAction.MOVE_RIGHT:
    pass
  elif action == PlayerAction.INTERACT:
    pass
  elif action == PlayerAction.ABILITY:
    pass
  elif action == PlayerAction.INVENTORY:
    pass
  elif action == PlayerAction.NO_ACTION:
    pass
  else:
    raise ValueError('Invalid player action encountered')

game_state = GameState()
