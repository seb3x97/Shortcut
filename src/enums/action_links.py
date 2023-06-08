#---------- Package ----------#

import enum

# Enum ActionLinks
class ActionLinks(enum.Enum):
    # Keyboard
    KEYBOARD_PRESS = 'keyboard_press'
    KEYBOARD_RELEASE = 'keyboard_release'
    KEYBOARD_TAP = 'keyboard_tap'
    KEYBOARD_TYPE = 'keyboard_type'

    # Mouse
    MOUSE_CLICK = 'mouse_click'
    MOUSE_MOVE_TO = 'mouse_move_to'
    MOUSE_MOVE = 'mouse_move'
    MOUSE_SCROLL = 'mouse_scroll'

    # Mode
    MODE_NORMAL = 'mode_normal'
    MODE_CREATIVE = 'mode_creative'

    # Other
    OTHER_DEBUG = 'other_debug'
    OTHER_DRAW = 'other_draw'
    OTHER_EXIT = 'other_exit'
    OTHER_SLEEP = 'other_sleep'
    OTHER_UPDATE = 'other_update'

    OTHER_CUSTOM = 'other_custom'
    OTHER_SAVE_CUSTOM = 'other_save_custom'