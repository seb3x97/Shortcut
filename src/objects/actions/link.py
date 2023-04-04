#---------- Package ----------#

from __future__ import annotations

#---------- Locals ----------#

# Keyboard
import src.objects.actions.keyboard.press as press
import src.objects.actions.keyboard.release as release
import src.objects.actions.keyboard.tap as tap
import src.objects.actions.keyboard.type as type

# Mouse
import src.objects.actions.mouse.click as click
import src.objects.actions.mouse.move_to as move_to
import src.objects.actions.mouse.move as move
import src.objects.actions.mouse.scroll as scroll

# Mode
import src.objects.actions.mode.normal as normal
import src.objects.actions.mode.creative as creative

# Other
import src.objects.actions.other.draw as draw
import src.objects.actions.other.sleep as sleep
import src.objects.actions.other.update as update

# Liste des liens des actions
action_links = {
    # Keyboard
    'keyboard_press': press.ActionKeyboardPress,
    'keyboard_release': release.ActionKeyboardRelease,
    'keyboard_tap': tap.ActionKeyboardTap,
    'keyboard_type': type.ActionKeyboardType,

    # Mouse
    'mouse_click': click.ActionMouseClick,
    'mouse_move_to': move_to.ActionMouseMoveTo,
    'mouse_move': move.ActionMouseMove,
    'mouse_scroll': scroll.ActionMouseScroll,

    # Mode
    'mode_normal': normal.ActionModeNormal,
    'mode_creation': creative.ActionModeCreative,

    # Other
    'other_draw': draw.ActionOtherDraw,
    'other_sleep': sleep.ActionOtherSleep,
    'other_update': update.ActionOtherUpdate,
}