class EntityClass:
  """Each entity belongs to one or more entity classes.  This should
  be useful in filtering entities by some property."""

  def __init__(self, class_name = None, attributes = None):
    if class_name is None:
      self.class_name = "invalid"
    else:
      self.class_name = class_name

    if attributes is None:
      self.attributes = {}
    else:
      self.attributes = attributes

MOVABLE_ENTITY_CLASS = EntityClass("movable")
IMMOVABLE_ENTITY_CLASS = EntityClass("immovable")
WEARABLE_ENTITY_CLASS = EntityClass("wearable")
WEAPON_ENTITY_CLASS = EntityClass("weapon", {'attack': 10})
EDIBLE_ENTITY_CLASS = EntityClass("edible")

class EntityType:
  """Each entity can only have one entity type."""

  def __init__(self, type_name = None, entity_classes = None):
    self.entity_classes = entity_classes
    self.actions = None
    self.attributes = {}
    if self.entity_classes is not None:
      for entity_class in self.entity_classes:
        self.set_attributes_from_entity_class(entity_class)

    if type_name is None:
      self.type_name = "invalid"
    else:
      self.type_name = type_name

  def set_attributes_from_entity_class(self, entity_class):
    attributes = entity_class.attributes
    print "Setting attributes from entity class = %s" % (entity_class.class_name)
    for attribute_name in attributes:
      if attribute_name in self.attributes:
        raise KeyError("The same attribute cannot be set by more than one "
                       "entity class. The guilty attribute is: '%s', being "
                       "set by entity class: '%s'." % (attribute_name, entity_class.class_name))
      self.attributes[attribute_name] = attributes[attribute_name]

class EntityModifier:
  def __init__(self, modifier_name = None):
    self.modifier_name = modifier_name

  def apply_modifier_to_entity(self, entity):
    pass

class CursedWeaponModifier(EntityModifier):
  def apply_modifier_to_entity(self, entity):
    entity.attributes['attack'] *= 0.8
    entity.attributes['can_drop'] = False

class BlessedWeaponModifier(EntityModifier):
  def apply_modifier_to_entity(self, entity):
    entity.attributes['attack'] *= 1.2
    entity.attributes['can_drop'] = True

# Modifiers are additional properties of items which can change how
# the item behaves. For example, if a sword has a `cursed' modifier,
# the modifier would:
# 1. Reduce the attack of the sword, and
# 2. Prevent the player from dropping the sword.

ELF_ENTITY_TYPE = EntityType("weapon")
VELVET_ARMOR_ENTITY_TYPE = EntityType("armor")

class Entity:
  def __init__(self, entity_type = None, entity_modifiers = None):
    self.entity_type = entity_type
    self.actions = self.entity_type.actions
    self.attributes = entity_type.attributes
    self.add_modifiers(entity_modifiers)

  def add_modifiers(self, entity_modifiers):
    if entity_modifiers is None:
      self.entity_modifiers = None
      return
    self.entity_modifiers = entity_modifiers
    self.update_attributes_using_modifiers(entity_modifiers)

  def update_attributes_using_modifiers(self, entity_modifiers):
    for entity_modifier in entity_modifiers:
      entity_modifier.apply_modifier_to_entity(self)

if __name__ == "__main__":
  # Examples
  RANGED_WEAPON_ENTITY_CLASS = EntityClass('ranged_weapon', {'attack_range': 5,})
  EXTRA_STRONG_WEAPON_MODIFIER = BlessedWeaponModifier("blessed_weapon_modifier")
  CROSSBOW_ENTITY_TYPE = EntityType("crossbow", [WEAPON_ENTITY_CLASS,
                                                 RANGED_WEAPON_ENTITY_CLASS])

  some_crossbow_entity = Entity(CROSSBOW_ENTITY_TYPE, [EXTRA_STRONG_WEAPON_MODIFIER])

  print
  print "Crossbow belongs to the entity classes: %s" % (map(lambda x: x.class_name, some_crossbow_entity.entity_type.entity_classes))
  print "Crossbow has the entity modifiers: %s" % (map(lambda x: x.modifier_name, some_crossbow_entity.entity_modifiers))
  print "Crossbow attack: %s" % (some_crossbow_entity.attributes['attack'])
  print "Crossbow range: %s" % (some_crossbow_entity.attributes['attack_range'])
  print "Crossbow can_drop: %s" % (some_crossbow_entity.attributes['can_drop'])
