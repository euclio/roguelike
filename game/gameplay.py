from map import make_empty_grid, Map

game_state = GameState()

def handle_gameplay():
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

class GameState(object):
  class Player:
    def __init__(self):
      self.location = (10, 10)

  def __init__(self):
    self.tile_map = Map(make_empty_grid(25, 25))
    self.player = Player()
