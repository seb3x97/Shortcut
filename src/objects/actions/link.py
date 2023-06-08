#---------- Package ----------#

from __future__ import annotations

#---------- Locals ----------#

# Links
from src.enums.action_links import ActionLinks

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
import src.objects.actions.other.debug as debug
import src.objects.actions.other.draw as draw
import src.objects.actions.other.exit as exit
import src.objects.actions.other.sleep as sleep
import src.objects.actions.other.update as update

import src.objects.actions.other.save_custom as save_custom

# Liste des liens des actions
action_links = {
    # Keyboard
    ActionLinks.KEYBOARD_PRESS.value: press.ActionKeyboardPress,
    ActionLinks.KEYBOARD_RELEASE.value: release.ActionKeyboardRelease,
    ActionLinks.KEYBOARD_TAP.value: tap.ActionKeyboardTap,
    ActionLinks.KEYBOARD_TYPE.value: type.ActionKeyboardType,

    # Mouse
    ActionLinks.MOUSE_CLICK.value: click.ActionMouseClick,
    ActionLinks.MOUSE_MOVE_TO.value: move_to.ActionMouseMoveTo,
    ActionLinks.MOUSE_MOVE.value: move.ActionMouseMove,
    ActionLinks.MOUSE_SCROLL.value: scroll.ActionMouseScroll,

    # Mode
    ActionLinks.MODE_NORMAL.value: normal.ActionModeNormal,
    ActionLinks.MODE_CREATIVE.value: creative.ActionModeCreative,

    # Other
    ActionLinks.OTHER_DEBUG.value: debug.ActionOtherDebug,
    ActionLinks.OTHER_DRAW.value: draw.ActionOtherDraw,
    ActionLinks.OTHER_EXIT.value: exit.ActionOtherExit,
    ActionLinks.OTHER_SLEEP.value: sleep.ActionOtherSleep,
    ActionLinks.OTHER_UPDATE.value: update.ActionOtherUpdate,

    ActionLinks.OTHER_SAVE_CUSTOM.value: save_custom.ActionOtherSaveCustom,
}