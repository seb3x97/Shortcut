#---------- Package ----------#

from typing import Union
from pynput import keyboard

#---------- Locals ----------#

from src.objects.listeners.listener import Listener

# Class ListenerKeyboard
class ListenerKeyboard(Listener):
    # Default Constructor
    def __init__(self):
        # Parent
        super().__init__()

        # Events
        self.on_press: function = None                      # Evenement => touche pressée
        self.on_release: function = None                    # Evenement => touche relachée

        # Controller
        self.__controller: keyboard.Controller = keyboard.Controller()

        # Listener
        self.__listener: keyboard.Listener = keyboard.Listener(
            on_press=self.__on_press,
            on_release=self.__on_release)


    #---------- Static ----------#

    # On récupére le code d'une touche (Virtual Key)
    @staticmethod
    def get_vk_code(key: Union[keyboard.KeyCode, keyboard.Key]) -> Union[int, None]:
        match type(key):
            case keyboard.KeyCode: return key.vk
            case keyboard.Key: return key.value.vk
            case _: return None

    # On récupére le KeyCode à partir d'un vk (Virtual Key)
    @staticmethod
    def get_key_code(code: int) -> keyboard.KeyCode:
        return keyboard.KeyCode.from_vk(code)


    #---------- Herited ----------#

    # On démarre le listener
    def start(self) -> bool:
        self.__listener.start()

        # Succès
        return True

    # On arrête le listener
    def stop(self) -> bool:
        self.__listener.stop()

        # Succès
        return True


    #---------- Functions ----------#

    # On appuie sur une touche
    def press(self, code: int):
        self.__controller.press(key=self.get_key_code(code=code))

    # On relâche une touche
    def release(self, code: int):
        self.__controller.release(key=self.get_key_code(code=code))
    
    # On tap une touche (press + release)
    def tap(self, code: int):
        self.__controller.tap(key=self.get_key_code(code=code))

    # On écrit du texte
    def type(self, text: str):
        self.__controller.type(string=text)


    #---------- Events ----------#

    # Event quand une touche est appuyée
    def __on_press(self, key: Union[keyboard.KeyCode, keyboard.Key]):
        # On essaye de récupére le code de la clé
        code: int = self.get_vk_code(key=key)
        if code is None: return

        # On trigger l'event "press"
        if not self.on_press is None: self.on_press(code)

    # Event quand une touche est relachée
    def __on_release(self, key: Union[keyboard.KeyCode, keyboard.Key]):
        # On essaye de récupére le code de la clé
        code: int = self.get_vk_code(key=key)
        if code is None: return

        # On trigger l'event "release"
        if not self.on_release is None: self.on_release(code)