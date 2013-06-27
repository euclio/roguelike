class PlayerAction:
    MOVE_UP = 1
    MOVE_DOWN = 2
    MOVE_LEFT = 3
    MOVE_RIGHT = 4
    INTERACT = 5
    ABILITY = 6
    INVENTORY = 7
    CANCEL = 8
    NO_ACTION = 9

_DEFAULT_KEYBINDINGS = {
        'w': PlayerAction.MOVE_UP,
        '8': PlayerAction.MOVE_UP,
        'a': PlayerAction.MOVE_LEFT,
        '4': PlayerAction.MOVE_LEFT,
        's': PlayerAction.MOVE_DOWN,
        '2': PlayerAction.MOVE_DOWN,
        'd': PlayerAction.MOVE_RIGHT,
        '6': PlayerAction.MOVE_RIGHT,
        'e': PlayerAction.INTERACT,
        'f': PlayerAction.ABILITY,
        'q': PlayerAction.INVENTORY,
        'z': PlayerAction.CANCEL,
}

keybindings = _DEFAULT_KEYBINDINGS

def handle_input(input_key):
    return keybindings.get(input_key, PlayerAction.NO_ACTION)
