#---------- Package ----------#

from __future__ import annotations
import pynput.mouse as py_mouse

#---------- Locals ----------#

import src.objects.handler.handler as Handler
import src.utils.custom_thread as CustomThread

# Utils
import src.utils.utils as Utils
import src.utils.paths as Paths
import src.utils.json_names as JsonNames

# Command
import src.objects.command.command as Command
import src.objects.actions.action as Action
import src.objects.actions.link as Link

# Class Mode
class Mode():
    # Default Constructor
    def __init__(self, handler: Handler.Handler) -> None:
        # Default
        self.thread: CustomThread.CustomThread = None
        #
        self.commands: dict[tuple, Command.Command] = {}                            # Liste des commandes

        # On enregistre
        self._handler: Handler.Handler = handler

    # On initialise le mode
    def init(self) -> bool:

        # Succès
        return True

    # On démarre le mode
    def start(self) -> bool:
        # Check si il n'y a pas de processus en court
        if not self.thread is None and self.thread.is_alive(): return False

        # On démarre le thread
        self.thread = CustomThread.CustomThread(target=self.exec, args=())
        self.thread.start()

        # Succès
        return True

    # On arrête le mode
    def stop(self) -> bool:
        # Check si il y a un processus en court
        if self.thread is None or not self.thread.is_alive(): return False

        # On termine le thread
        self.thread.stop()

        # Succès
        return True
    
    # On récupére les données (json)
    def get_commands(self) -> bool:
        # Checks si le chemin du fichier éxiste
        if not self.path_config: return False

        # On essaye de récupérer le contenu du fichier
        content: str = Utils.read_file_content(self.path_config)
        if content is None: return False

        # On essaye de convertir le contenu en dictionnaire (json)
        datas: dict = Utils.convert_text_to_json(content)
        if datas is None: return False

        # On supprime les anciennes commandes
        self.commands.clear()

        # On boucle les commandes
        for data in datas:
            command_name: str = JsonNames.get_command_name(data)
            command_shortcut: tuple = JsonNames.get_command_shortcut(data)
            command_actions: list[Action.Action] = []

            # On boucle les actions
            for action in JsonNames.get_command_actions(data):
                class_name: str = JsonNames.get_command_action_class(action)
                class_args: dict[str, object] = JsonNames.get_command_action_args(action)
                
                # On essaye de récupére la classe de l'action
                action_class: Action = Link.action_links.get(class_name, None)
                if action_class is None:
                    print("Nom de la classe introuvable")
                    return False

                # On essaye d'instancier et de sauvegarder les données de l'action
                action: Action.Action = action_class(self)
                if not action.save_datas(class_args):
                    print("Impossible d'enregistrer des arguments")
                    return False

                # On ajoute l'action à la liste des actions
                command_actions.append(action)

            # Si la commande éxiste déjà on retourne
            if command_shortcut in self.commands: return False

            # On crée et ajoute la commande à la liste des commandes
            command: Command.Command = Command(command_name, command_shortcut, command_actions)
            self.commands[command_shortcut] = command

        # Succès
        return True
    
    # -- Abstract Function -- #

    # Execution du code
    def init(): raise NotImplementedError()
    def exec(): raise NotImplementedError()

    # Events du clavier
    def on_press(self, code: int, new: bool): pass
    def on_release(self, code: int): pass
    def on_shortcut(self, codes: list[int], new: bool): pass

    # Events de la souris
    def on_move(self, x: int, y: int): pass
    def on_click(self, x: int, y: int, button: py_mouse.Button, pressed: bool): pass
    def on_scroll(self, x: int, y: int, dx: int, dy: int): pass