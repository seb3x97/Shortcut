#---------- Package ----------#

import time
from PIL import Image
from pynput import mouse

#---------- Locals ----------#

from src.objects.actions.action import Action
from src.objects.enums.virtual_keys import VirtualKeys

# Class ActionOtherDraw
class ActionOtherDraw(Action):
    # Constructeur Renseigné
    def __init__(self, startup) -> None:
        # Parent
        super().__init__(startup)

        self.src = ""

    # On démarre l'action
    def start(self) -> bool:

        img = Image.open(self.src)
        img = img.convert('P', palette=Image.Palette.ADAPTIVE, colors=50).convert('RGBA')

        width, height = img.size

        init_x, init_y = (1961, 181) #self._startup.mouse_manager.get_mouse_pos()

        colors: dict[tuple, list[tuple]] = {}

        for x in range(width):
            for y in range(height):
                # On récupére les couleurs rgba/rgb
                color_rgba: tuple = img.getpixel((x, y))
                color_rgb: tuple = color_rgba[:-1]

                # Checks des couleurs
                if color_rgba[-1] == 0: continue                                # Si la couleur est transparente
                if sorted(color_rgb) == sorted((255, 255, 255)): continue       # Si la couleur est blanche

                # On ajoute la couleur dans le dictionnaire
                if(color_rgb not in colors): colors[color_rgb] = []
                colors[color_rgb].append((x, y))


        for color in colors:
            positions = colors[color]

            self._startup.mouse_manager.move_to(3040, 69)
            self._startup.mouse_manager.click(mouse.Button.left, 2)
            time.sleep(1)

            POSITIONS = [
                (3077, 594),
                (3077, 612),
                (3077, 642),
            ]

            for i in range(len(color)):
                x, y = POSITIONS[i]
                self._startup.mouse_manager.move_to(x, y)
                self._startup.mouse_manager.click(mouse.Button.left, 2)
                time.sleep(0.1)

                text = str(color[i])
                for char in text:
                    vk_name = f"VK_{char}"
                    value = VirtualKeys[vk_name].value
                    self._startup.keyboard_manager.tap(value)
                    time.sleep(0.1)

            self._startup.mouse_manager.move_to(2695, 665)
            self._startup.mouse_manager.click(mouse.Button.left, 2)
            time.sleep(0.1)

            count = 0
            for position in positions:
                x, y = position
                self._startup.mouse_manager.move_to(init_x + x, init_y + y)
                self._startup.mouse_manager.click(mouse.Button.left, 1)
                time.sleep(0.001)

                count += 1

            time.sleep(0.5)

        # Succès
        return True

    # On arrête l'action
    def stop(self) -> bool:
        # Succès
        return True