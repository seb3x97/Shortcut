#---------- Locals ----------#

# Managers
import src.objects.managers.keyboard as Keyboard
import src.objects.managers.mouse as Mouse

# Command
import src.objects.command.command as Command
import src.objects.actions.action as Action
import src.objects.actions.link as Link

# Modes
import src.objects.modes.mode as Mode
import src.objects.enums.mode_type as ModeType

# Utils
import src.utils.utils as Utils
import src.utils.paths as Paths
import src.utils.json_names as JsonNames

# Class Startup
class Startup():
    # Default Constructor
    def __init__(self) -> None:
        # -- Default -- #
        self.keyboard_manager: Keyboard.ManagerKeyboard = Keyboard.ManagerKeyboard()        # Manager du clavier
        self.mouse_manager: Mouse.ManagerMouse = Mouse.ManagerMouse()                       # Manager de la souris
        #
        self.modes: dict[ModeType.ModeType, Mode.Mode] = {}                                 # Dictionnaire de tous les modes
        self.mode: Mode = None                                                              # Mode actuel
        #
        self.commands: dict[tuple, Command.Command] = {}                                    # Liste des commandes

    # On initialise la classe
    def init(self) -> bool:
        # On enregistre les modes
        self.modes = {key: value(self) for key, value in ModeType.MODES.items()}

        # On essaye de lire les données des commandes
        if not self.get_commands(): return False

        # Succès
        return True

    # On démarre
    def start(self) -> bool:
        # On essaye de faire démarrer les managers
        if not self.keyboard_manager.start(): return False
        if not self.mouse_manager.start(): return False
        if not self.change_mode(ModeType.ModeType.NORMAL): return False

        # Succès
        return True

    # On arrête
    def stop(self) -> bool:
        self.keyboard_manager.stop()
        self.mouse_manager.stop()
        self.mode.stop()

        # Succès
        return True

    # On récupére les données (json)
    def get_commands(self) -> bool:
        # On essaye de récupérer le contenu du fichier
        content: str = Utils.read_file_content(Paths.FILE_COMMAND_DEFAULT)
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
                action: Action = action_class(self)
                if not action.save_datas(class_args):
                    print("Impossible d'enregistrer des arguments")
                    return False

                # On ajoute l'action à la liste des actions
                command_actions.append(action)

            # Si la commande éxiste déjà on retourne
            if command_shortcut in self.commands: return False

            # On crée et ajoute la commande à la liste des commandes
            command: Command = Command(command_name, command_shortcut, command_actions)
            self.commands[command_shortcut] = command

        # Succès
        return True

    # On enregistre le mode
    def change_mode(self, mode_type: ModeType, args: tuple = ()) -> bool:
        # On stop l'ancien mode
        if not self.mode is None: self.mode.stop()

        # On essaye d'enregistrer le nouveau mode
        self.mode: Mode = self.modes.get(mode_type, None)
        if self.mode is None: return False

        # Events du clavier
        self.keyboard_manager.on_press = self.mode.on_press
        self.keyboard_manager.on_release = self.mode.on_release
        self.keyboard_manager.on_shortcut = self.mode.on_shortcut

        # Events de la souris
        self.mouse_manager.on_move = self.mode.on_move
        self.mouse_manager.on_click = self.mode.on_click
        self.mouse_manager.on_scroll = self.mode.on_scroll

        # On essaye de démarrer le mode
        if not self.mode.init(*args): return False
        if not self.mode.start(): return False

        # Succès
        return True