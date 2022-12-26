#---------- Locals ----------#

import src.utils.utils_class as utils_class

# Class Action
class Action:
    # Default Constructor
    def __init__(self, startup) -> None:
        from src.startup import Startup

        # On enregistre
        self._startup: Startup = startup


    #---------- Herited ----------#

    # On démarre l'action
    def start(self) -> bool: raise NotImplementedError()

    # On arrête l'action
    def stop(self) -> bool: raise NotImplementedError()


    #---------- Functions ----------#

    # On sauvegarde les données
    def save_datas(self, datas: dict[str, object]):
        return utils_class.save_class_public_variables_with_values(self, datas)

    # On récupére les données
    def to_datas(self) -> dict[str, object]:
        return utils_class.get_class_public_variables_with_values(self)