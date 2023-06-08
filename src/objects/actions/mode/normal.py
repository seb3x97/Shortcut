#---------- Package ----------#

from __future__ import annotations

#---------- Locals ----------#

import src.objects.actions.action as action

# Class ActionModeNormal
class ActionModeNormal(action.Action):
    # Constructeur Renseigné
    def __init__(self, handler) -> None:
        # Parent
        super().__init__(handler)

    # On démarre l'action
    def start(self) -> bool:
        # On essaye de changer le mode
        import src.enums.mode_type as ModeType
        if not self._handler.start_mode(mode_type=ModeType.ModeType.NORMAL): return False

        # Succès
        return True

    # On arrête l'action
    def stop(self) -> bool:
        # Succès
        return True