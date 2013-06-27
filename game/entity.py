class EntityClass:
  """Each entity belongs to one or more entity classes.  This should
  be useful in filtering entities by some property."""

  def __init__(self, class_name = None):
    if class_name is None:
      self.class_name = "invalid"
    else:
      self.class_name = class_name

MOVABLE_ENTITY_CLASS = EntityClass("movable")
IMMOVABLE_ENTITY_CLASS = EntityClass("immovable")
WEARABLE_ENTITY_CLASS = EntityClass("wearable")
WEAPON_ENTITY_CLASS = EntityClass("weapon")
EDIBLE_ENTITY_CLASS = EntityClass("edible")

# Entities may boost or reduce player attributes when
# used/wielded/carried. How do we represent this?

# Also, each entity instance should have specific attributes such as
# name, HP, hunger, gender, etc. Different kinds of entities have
# different kinds of attributes. How do we define a 'kind of entity'?
# EntityType + [EntityClass list]?

class EntityType:
  """Each entity can only have one entity type."""

  def __init__(self, type_name = None, entity_classes = None):
    self.entity_classes = entity_classes

    if type_name is None:
      self.type_name = "invalid"
    else:
      self.type_name = type_name

# Modifiers are additional properties of items which can change how
# the item behaves. For example, if a sword has a `cursed' modifier,
# the modifier would:
# 1. Reduce the attack of the sword, and
# 2. Prevent the player from dropping the sword.

# class Modifier:
#   def __init__(self):
#     pass
#
#   def apply_effects(self, entity):
#     pass

# class CursedModifier(Modifier):
#   def apply_effects(self, entity):
#     entity.removable = False

# class CursedWeaponModifier(CursedModifier):
#   def apply_effects(self, entity):
#     super.apply_effects(entity)
#     entity.attack *= 0.8

PLAYER_ENTITY_TYPE = EntityType("player")
ELF_ENTITY_TYPE = EntityType("weapon")
VELVET_ARMOR_ENTITY_TYPE = EntityType("armor")

class Entity:
  def __init__(self, entity_type = None, entity_id = None):
    self.entity_type = entity_type
    self.entity_id = entity_id
