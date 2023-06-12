#---------- Package ----------#

from __future__ import annotations

#---------- Locals ----------#

import src.objects.managers.manager as Manager
import src.objects.listeners.keyboard as Keyboard

# Class ManagerKeyboard
class ManagerKeyboard(Manager.Manager):
    # Default Constructor
    def __init__(self):
        # Parent
        super().__init__()

        # -- Default -- #
        self.__enable_events: bool = True                   # active/désactive les évenements
        self.__being_pressed_key_code: list = []            # Liste des touches qui sont entrain d'être appuyé
        self.__current_shortcut_key_code: list = []         # Liste des touches qui forment un raccourci

        # Events
        self.on_press: function = None                      # Evenement => touche pressée
        self.on_release: function = None                    # Evenement => touche relachée
        self.on_shortcut: function = None                   # Evenement => Raccourci éxecutée

        # Listener + ajout des events
        self.__keyboard_listner: Keyboard.ListenerKeyboard = Keyboard.ListenerKeyboard()
        self.__keyboard_listner.on_press = self.__on_press
        self.__keyboard_listner.on_release = self.__on_release


    #---------- Herited ----------#

    # On démarre le listener
    def start(self) -> bool:
        return self.__keyboard_listner.start()

    # On arrête le listener
    def stop(self) -> bool:
        return self.__keyboard_listner.stop()
    
    # On join le listener
    def join(self) -> bool:
        return self.__keyboard_listner.join()


    #---------- Functions ----------#

    # On appuie sur une touche
    def press(self, code: int):
        self.__enable_events = False
        self.__keyboard_listner.press(code=code)
        self.__enable_events = True

    # On relâche une touche
    def release(self, code: int):
        self.__enable_events = False
        self.__keyboard_listner.release(code=code)
        self.__enable_events = True
    
    # On tap une touche (press + release)
    def tap(self, code: int):
        self.__enable_events = False
        self.__keyboard_listner.tap(code=code)
        self.__enable_events = True

    # On écrit du texte
    def type(self, text: str):
        self.__enable_events = False
        self.__keyboard_listner.type(text=text)
        self.__enable_events = True


    #---------- Events ----------#

    # Event quand une touche est appuyée
    def __on_press(self, code: int):
        # Check si les evenements sont activés
        if not self.__enable_events: return

        # Si le code n'est pas déjà dans la liste
        new_key = not code in self.__being_pressed_key_code

        # 1) On ajoute le code à la liste des touches qui sont entrains d'être appuyés
        # 2) On ajoute le code à la liste des raccourcis
        if new_key:
            self.__being_pressed_key_code.append(code)
            self.__current_shortcut_key_code.append(code)

        # On trigger l'event "press" et "shortcut"
        if not self.on_press is None: self.on_press(code, new_key)
        if not self.on_shortcut is None: self.on_shortcut(self.__current_shortcut_key_code, new_key)

    # Event quand une touche est relachée
    def __on_release(self, code: int):
        # Check si les evenements sont activés
        if not self.__enable_events: return

        # Si le code est dans la liste des touches qui sont entrains d'être appuyés on le retire de la liste
        if code in self.__being_pressed_key_code: self.__being_pressed_key_code.remove(code)

        # On trigger l'event realease
        if not self.on_release is None: self.on_release(code)
        
        # On clear la liste des touches pour le raccourci actuelle
        self.__current_shortcut_key_code.clear()