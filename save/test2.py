import keyboard


class Shortcut:

    def __init__(self) -> None:
        pass

    def start(self) -> None:
        keyboard.
        keyboard.on_press(callback=self.test)
        keyboard.on_release(callback=self.callback)
        keyboard.wait()

    def test(self, event: keyboard.KeyboardEvent):
        print("t" + event.name)

    # Invoqué quand un event du clavier se produit
    def callback(self, event: keyboard.KeyboardEvent):
        # On essaye de récupérer le nom de l'event
        name: str = event.name
        if name is None: return

        print("c" + name)

    # On convertit le nom d'une touche en texte
    # Ex : decimal => .
    def convert_name_to_text(name: str) -> str:
        # Texte de sortie
        text: str = name

        # On check les charactères spéciaux
        match name:
            case "space":   text = " "              # Espace
            case "enter":   text = "\n"             # Enter
            case "decimal": text = "."              # Decimal
            case _:         text = ""               # Default

        # On retourne le texte convertit
        return text







if __name__ == "__main__":
    shortcut = Shortcut()
    shortcut.start()