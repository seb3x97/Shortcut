#---------- Package ----------#

from __future__ import annotations
import enum

#---------- Locals ----------#

import src.objects.modes.mode as mode
import src.objects.modes.normal as normal
import src.objects.modes.creative as creative
import src.objects.modes.action as action

# Enum ModeType
class ModeType(enum.Enum):
    NORMAL      = 10
    CREATIVE    = 20
    ACTION      = 30

# Liste des modes
MODES: dict[int, mode.Mode] = {
    ModeType.NORMAL:    normal.ModeNormal,
    ModeType.CREATIVE:  creative.ModeCreative,
    ModeType.ACTION:    action.ModeAction,
}