#---------- Package ----------#

from enum import Enum

#---------- Locals ----------#

from src.objects.modes.mode import Mode
from src.objects.modes.normal import ModeNormal
from src.objects.modes.creative import ModeCreative
from src.objects.modes.action import ModeAction

# Class ModeType
class ModeType(Enum):
    NORMAL      = 10
    CREATIVE    = 20
    ACTION      = 30

# Liste des modes
MODES: dict[int, Mode] = {
    ModeType.NORMAL:    ModeNormal,
    ModeType.CREATIVE:  ModeCreative,
    ModeType.ACTION:    ModeAction,
}