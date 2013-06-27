from entity import *

class PlayerEntity(Entity):
  def print_something(self, s):
    print "This is player printing what you asked for: %s!" % (s)

  def move_up(self):
    y, x = self.location
    self.location = y - 1, x

  def move_left(self):
    y, x = self.location
    self.location = y, x - 1

  def move_right(self):
    y, x = self.location
    self.location = y, x + 1

  def move_down(self):
    y, x = self.location
    self.location = y + 1, x

  def is_on_map(self):
    return True

  def __init__(self, location):
    self.location = location
    self.kind = 'player'
