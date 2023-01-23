from src.objects.modes.action import ModeAction

from src.objects.actions.mouses.click import ActionMouseClick
from src.objects.actions.mouses.move_to import ActionMouseMoveTo
import time


liste = [
    ActionMouseMoveTo(3420, 22),
    ActionMouseClick(1, 0),
    ActionMouseMoveTo(3193, 20),
    ActionMouseClick(1, 0),
    ActionMouseMoveTo(2974, 18),
    ActionMouseClick(1, 0),
]


if __name__ == '__main__':
    action = ModeAction(liste)
    action.start()

    time.sleep(7)
    action.stop()
    print("end")
