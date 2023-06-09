#---------- Package ----------#

from __future__ import annotations

#---------- Locals ----------#

import src.objects.actions.action as action
import src.utils.utils as utils

# Class ActionOtherSaveCustom
class ActionOtherSaveCustom(action.Action):
    # Constructeur Renseigné
    def __init__(self, handler) -> None:
        # Parent
        super().__init__(handler)

    # On démarre l'action
    def start(self) -> bool:
        # Check si le dernier mode est défini
        if self._handler.mode._last_mode is None: return False

        # todo : check si l'ancien mode c'est le creatif

        from src.objects.configs.childs.command import ConfigChildCommand
        from src.objects.configs.childs.action import ConfigChildAction

        #actions = list(map((lambda action: ConfigChildAction(**action)), self._handler.mode._last_mode.custom_actions))

        command = ConfigChildCommand('test', (162, 165, 77), self._handler.mode._last_mode.custom_actions)

        self._handler.config.custom.commands.clear()
        self._handler.config.custom.commands.append(command)

        self._handler.config.save_config_custom()

        # Succès
        return True

    # On arrête l'action
    def stop(self) -> bool:
        # Succès
        return True