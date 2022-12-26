#---------- Locals ----------#

# Keyboard
from src.objects.actions.keyboard.press import ActionKeyboardPress
from src.objects.actions.keyboard.release import ActionKeyboardRelease
from src.objects.actions.keyboard.tap import ActionKeyboardTap
from src.objects.actions.keyboard.type import ActionKeyboardType

# Mouse
from src.objects.actions.mouse.click import ActionMouseClick
from src.objects.actions.mouse.move_to import ActionMouseMoveTo
from src.objects.actions.mouse.move import ActionMouseMove
from src.objects.actions.mouse.scroll import ActionMouseScroll

# Other
from src.objects.actions.other.draw import ActionOtherDraw
from src.objects.actions.other.sleep import ActionOtherSleep
from src.objects.actions.other.update import ActionOtherUpdate

# Liste des liens des actions
action_links = {
    # Keyboard
    'keyboard_press': ActionKeyboardPress,
    'keyboard_release': ActionKeyboardRelease,
    'keyboard_tap': ActionKeyboardTap,
    'keyboard_type': ActionKeyboardType,

    # Mouse
    'mouse_click': ActionMouseClick,
    'mouse_move_to': ActionMouseMoveTo,
    'mouse_move': ActionMouseMove,
    'mouse_scroll': ActionMouseScroll,

    # Other
    'other_draw': ActionOtherDraw,
    'other_sleep': ActionOtherSleep,
    'other_update': ActionOtherUpdate,
}