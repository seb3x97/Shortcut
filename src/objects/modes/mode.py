#---------- Package ----------#

from __future__ import annotations
import pynput.mouse as py_mouse

#---------- Locals ----------#

import src.objects.handler.handler as Handler
import src.utils.custom_thread as CustomThread

# Utils
import src.utils.utils as Utils
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
        
        # Default
        self._commands: dict[tuple, Command.Command] = {}
        self._last_mode: Mode = None

        # On enregistre
        self._handler: Handler.Handler = handler

    # On définit le dernier mode utilisé
    def set_last_mode(self, last_mode):
        # On enregistre le dernier mode
        self._last_mode = last_mode

        # Succès
        return True

    # On initialise le mode
    def init(self) -> bool:
        # On essaye de récupérer les commandes
        if not self.retrieve_commands(): return False

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

        # On supprime les anciennes commandes
        self._commands.clear()

        # Succès
        return True
    
    # On récupére les données (json)
    def retrieve_commands(self) -> bool:
        # Checks si le chemin du fichier éxiste
        if not self.path_config:
            print(f"Le mode actuel n'a pas de chemin de config")
            return False
        
        # todo :
        # On boucle les chemins de configuration
        for path in self.path_config:
            # On essaye de récupérer le contenu du fichier
            content: str = Utils.read_file_content(path)
            if content is None: return False

            # On essaye de convertir le contenu en dictionnaire (json)
            datas: dict = Utils.convert_text_to_json_object(content)
            if datas is None: return False

            # On boucle les commandes
            for data in datas['commands']:
                # On récupére les données dans la commande
                command_name: str = JsonNames.get_command_name(data)
                command_shortcut: tuple = JsonNames.get_command_shortcut(data)
                command_actions = JsonNames.get_command_actions(data)

                # Si la commande éxiste déjà
                if command_shortcut in self._commands:
                    print(f"Doublon du shortcut de la commande '{command_name}' et la commande '{self._commands.get(command_shortcut).name}'")
                    break

                # On crée et ajoute la commande à la liste des commandes
                command: Command.Command = self.convert_command_data_to_class(command_name, command_shortcut, command_actions)
                if command is None:
                    print(f"Une erreur est survenue l'hors du chargement de la commande '{command_name}'")
                    break

                # On enregistre la commande
                self._commands[command_shortcut] = command

        # Succès
        return True
    
    # On convertit les données d'une commande en un classe
    def convert_command_data_to_class(self, command_name: str, command_shortcut: tuple, command_actions: list) -> Command.Command:
        # Données
        name: str = command_name
        shortcut: tuple = command_shortcut
        actions: list[Action.Action] = []

        # On boucle les actions
        for action in command_actions:
            # On récupére les données de l'action
            class_name: str = JsonNames.get_command_action_class(action)
            class_args: dict[str, object] = JsonNames.get_command_action_args(action)
            
            # On essaye de récupére la classe de l'action
            action_class: Action = Link.action_links.get(class_name, None)
            if action_class is None:
                print(f"Nom de la classe '{class_name}' introuvable")
                return None

            # On essaye d'instancier et de sauvegarder les données de l'action
            action: Action.Action = action_class(self._handler)
            if not action.save_datas(class_args):
                print("Impossible d'enregistrer des arguments")
                return None

            # On ajoute l'action à la liste des actions
            actions.append(action)

        # Succès
        return Command.Command(name, shortcut, actions)
    

    #---------- Functions ----------#

    # On essaye de charger une action
    def load_action(self, code: tuple) -> bool:
        # On essaye de mettre le mode action
        import src.enums.mode_type as mode_type
        if not self._handler.start_mode(mode_type.ModeType.ACTION, [self._commands[code]]):
            print("Impossible de changer de mode")
            return False

        # Succès
        return True


    # -- Abstract Function -- #

    # Execution du code
    def set_args(): raise NotImplementedError()
    def exec(): raise NotImplementedError()

    # Events du clavier
    def on_press(self, code: int, new: bool): pass
    def on_release(self, code: int): pass
    def on_shortcut(self, codes: list[int], new: bool): pass

    # Events de la souris
    def on_move(self, x: int, y: int): pass
    def on_click(self, x: int, y: int, button: py_mouse.Button, pressed: bool): pass
    def on_scroll(self, x: int, y: int, dx: int, dy: int): pass