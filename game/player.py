from entity import *

class PlayerActions:
  def print_something(self, s):
    print "This is player printing what you asked for: %s!" % (s)

class PlayerEntityType(EntityType):
  def __init__(self, type_name = None, entity_classes = None):
    EntityType.__init__(self, type_name, entity_classes)
    self.actions = PlayerActions()

PLAYER_ENTITY_TYPE = PlayerEntityType("player")
PlayerEntity = Entity(PLAYER_ENTITY_TYPE)
PlayerEntity.actions.print_something("Hello!")
