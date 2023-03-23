import threading
import ctypes

# Class AbortableThread
class AbortableThread(threading.Thread):
    # Constructeur Renseigné
    def __init__(self, *args, **keywords):
        # Parent
        super().__init__(*args, **keywords)
        
    # On récupére l'identifiant du thread
    def get_id(self):
        # Check si le thread est démarré
        if not self.is_alive: return None

        # On retourne l'identifiant (système) du thread
        return self.native_id

    # On force le thread à s'arrêter en injectant une exception
    def abort(self) -> bool:
        # On essaye de récupérer l'identifiant du thread
        thread_id = self.get_id()
        if thread_id is None: return False

        # On essaye de fermer le thread
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread_id), ctypes.py_object(SystemExit))
        if res > 1: res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread_id), 0)
        if res > 1: return False

        # Succès
        return True