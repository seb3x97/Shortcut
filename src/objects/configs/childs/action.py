# Class ConfigChildAction
class ConfigChildAction:
    name: str
    args: dict

    def __init__(self, name: str, args: dict) -> None:
        self.name = name
        self.args = args