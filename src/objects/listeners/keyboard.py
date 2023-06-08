#---------- Package ----------#

from __future__ import annotations
import pynput.keyboard as py_keyboard
import typing

#---------- Locals ----------#

import src.objects.listeners.listener as Listener

# Class ListenerKeyboard
class ListenerKeyboard(Listener.Listener):
    # Default Constructor
    def __init__(self):
        # Parent
        super().__init__()

        # Events
        self.on_press: function = None                      # Evenement => touche pressée
        self.on_release: function = None                    # Evenement => touche relachée

        # Controller
        self.__controller: py_keyboard.Controller = py_keyboard.Controller()

        # Listener
        self.__listener: py_keyboard.Listener = py_keyboard.Listener(
            on_press=self.__on_press,
            on_release=self.__on_release)


    #---------- Static ----------#

    # On récupére le code d'une touche (Virtual Key)
    @staticmethod
    def get_vk_code(key: typing.Union[py_keyboard.KeyCode, py_keyboard.Key]) -> typing.Union[int, None]:
        match type(key):
            case py_keyboard.KeyCode: return key.vk
            case py_keyboard.Key: return key.value.vk
            case _: return None

    # On récupére le KeyCode à partir d'un vk (Virtual Key)
    @staticmethod
    def get_key_code(code: int) -> py_keyboard.KeyCode:
        return py_keyboard.KeyCode.from_vk(code)


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
    
    # On join le listener
    def join(self) -> bool:
        self.__listener.join()

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
    def __on_press(self, key: typing.Union[py_keyboard.KeyCode, py_keyboard.Key]):
        # On essaye de récupére le code de la clé
        code: int = self.get_vk_code(key=key)
        if code is None: return

        # On trigger l'event "press"
        if not self.on_press is None: self.on_press(code)

    # Event quand une touche est relachée
    def __on_release(self, key: typing.Union[py_keyboard.KeyCode, py_keyboard.Key]):
        # On essaye de récupére le code de la clé
        code: int = self.get_vk_code(key=key)
        if code is None: return

        # On trigger l'event "release"
        if not self.on_release is None: self.on_release(code)