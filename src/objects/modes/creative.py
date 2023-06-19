#---------- Package ----------#

from __future__ import annotations
import pynput.mouse as py_mouse
from datetime import datetime

#---------- Locals ----------#

from src.enums.action_links import ActionLinks
import src.utils.json_names as  json_names

import src.utils.paths as Paths
import src.objects.modes.mode as Mode

# Class ModeCreative
class ModeCreative(Mode.Mode):
    # Default Constructor
    def __init__(self, handler):
        # Parent
        super().__init__(handler)

        # Default
        self.path_config = [Paths.FILE_CONFIG_MODE_CREATIVE]

        # Default
        self.custom_actions = []
        self.last_action_time: datetime = None

        self.keyboard_keys_pressed: dict = {}

    # On sauvegarde les arguments
    def set_args(self) -> bool:
        # Succès
        return True

    # On éxécute les sous-tâches du mode
    def exec(self) -> bool:
        # Réinitialise
        self.custom_actions = []

        # Succès
        return True

    # On ajoute une commande aux commandes
    def add_command(self, name: ActionLinks, args: dict):
        self.custom_actions.append(json_names.create_action(
            name.value,
            args,
        ))
    
    # On rempli le trou entre les commandes
    def fill_gap(self):
        # On récupére le temps actuel
        current_time: datetime = datetime.now()
        
        # Si il y a déjà un temps on ajoute l'action de temps
        if(self.last_action_time != None):
            self.add_command(
                ActionLinks.OTHER_SLEEP,
                {
                    'secs': (current_time - self.last_action_time).total_seconds(),
                },
            )

        # On enregistre le temps actuel
        self.last_action_time = current_time
    
    # Event quand on appuie sur une touche
    def on_press(self, code: int, new: bool):
        # Si ce n'est pas une nouvelle touche on ne la prends pas en compte
        if not new: return

        # On passe le keyboard press à true
        if not code in self.keyboard_keys_pressed: self.keyboard_keys_pressed[code] = None

        # On rempli le gap avec une attente
        self.fill_gap()

        # On execute la commande
        self.add_command(
            ActionLinks.KEYBOARD_PRESS,
            {
                'code': code
            },
        )

    # Event quand on relâche une touche
    def on_release(self, code: int):
        # todo : meilleur com
        # Si on n'a pas encore appuyé sur le clavier ça veut dire
        # qu'on reçoit le relâchement des touches de la commande créatif
        if not code in self.keyboard_keys_pressed: return
        self.keyboard_keys_pressed.pop(code)

        # On rempli le gap avec une attente
        self.fill_gap()

        # On execute la commande
        self.add_command(
            ActionLinks.KEYBOARD_RELEASE,
            {
                'code': code
            },
        )

    # Event quand la souris bouge
    def on_move(self, x: int, y: int):
        # On rempli le gap avec une attente
        self.fill_gap()

        print(str(x) + " " + str(y))

        # On execute la commande
        self.add_command(
            ActionLinks.MOUSE_MOVE_TO,
            {
                'x': x,
                'y': y,
            },
        )

    # Event click de la souris
    def on_click(self, x: int, y: int, button: py_mouse.Button, pressed: bool):
        # On rempli le gap avec une attente
        self.fill_gap()

        # On execute la commande
        self.add_command(
            ActionLinks.MOUSE_CLICK,
            {
                'button': button.value,
                'count': 1,
            },
        )

    # Event scroll de la souris
    def on_scroll(self, x: int, y: int, dx: int, dy: int):
        # On rempli le gap avec une attente
        self.fill_gap()

        # On execute la commande
        self.add_command(
            ActionLinks.MOUSE_SCROLL,
            {
                'dx': dx,
                'dy': dy,
            },
        )

    #---------- Events ----------#

    # Event raccourci
    def on_shortcut(self, codes: list[int], new: bool):
        # On récupére le code unique
        code: tuple = tuple(codes)

        # Si le raccourci éxiste dans la liste des commandes
        if new and (code in self._commands):
            # todo : On enlève la commande des touches enregistrées
            # todo : faire un meilleur système
            numbers = len(code) * 2
            self.custom_actions = self.custom_actions[:-numbers]

            # On charge l'action
            self.load_action(code)
