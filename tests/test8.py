import threading
import ctypes
import time

"""
# Class AbortableThread
class AbortableThread(threading.Thread):
    # Constructeur Renseigné
    def __init__(self, *args, **keywords):
        # Parent
        super().__init__(*args, **keywords)

        self._kill = threading.Event()
        self._interval = 5

    def run(self):
        while True:
            print("Do Something")

            # If no kill signal is set, sleep for the interval,
            # If kill signal comes in while sleeping, immediately
            #  wake up and handle
            is_killed = self._kill.wait(self._interval)
            if is_killed:
                break

    def kill(self):
        self._kill.set()
        
    # On récupére l'identifiant du thread
    def get_id(self):
        # Check si le thread est démarré
        if not self.is_alive: return None

        # On retourne l'identifiant (python) du thread
        return self.ident

    # On force le thread à s'arrêter en injectant une exception
    def abort(self) -> bool:
        # On essaye de récupérer l'identifiant du thread
        thread_id = self.get_id()
        if thread_id is None: return False

        # On essaye de fermer le thread
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread_id), ctypes.py_object(SystemExit))

        # Si il renvoie un nombre supérieur à '1' c'est qu'il y a un problème.
        # On doit donc l'appeler à nouveau avec exc=NULL pour annuler l'effet
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread_id), None)
            return False

        # Succès
        return True
"""

"""
import sys
class AbortableThread(threading.Thread):
  def __init__(self, *args, **keywords):
    threading.Thread.__init__(self, *args, **keywords)
    self.killed = False

  def start(self):
    self.__run_backup = self.run
    self.run = self.__run      # Force the Thread to
    threading.Thread.start(self)

  def __run(self):
    sys.settrace(self.globaltrace)
    self.__run_backup()
    self.run = self.__run_backup

  def globaltrace(self, frame, why, arg):
    if why == 'call':
      return self.localtrace
    else:
      return None

  def localtrace(self, frame, why, arg):
    if self.killed:
      if why == 'line':
        raise SystemExit()
    return self.localtrace

  def kill(self):
    self.killed = True
    
def worker():
    print("start")
    time.sleep(10)
    print("end")
"""

# Class AbortableThread
class AbortableThread(threading.Thread):
    # Constructeur Renseigné
    def __init__(self, *args, **keywords):
        # Parent
        super().__init__(*args, **keywords)

        # Default
        self.event_kill = threading.Event()

    """
    def run(self):
        while True:
            print("Do Something")

            # If no kill signal is set, sleep for the interval,
            # If kill signal comes in while sleeping, immediately
            #  wake up and handle
            is_killed = self._kill.wait(self._interval)
            if is_killed:
                break
    """
        
    # On récupére l'identifiant du thread
    def get_id(self):
        # Check si le thread est démarré
        if not self.is_alive: return None

        # On retourne l'identifiant (python) du thread
        return self.ident

    # On attends que le thread soit dans une "safe zone" pour le kill
    def stop(self):
        self.event_kill.set()

    # On force le thread à s'arrêter en injectant une exception
    def kill(self) -> bool:
        # On essaye de récupérer l'identifiant du thread
        thread_id = self.get_id()
        if thread_id is None: return False

        # On essaye de fermer le thread
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread_id), ctypes.py_object(SystemExit))

        # Si il renvoie un nombre supérieur à '1' c'est qu'il y a un problème.
        # On doit donc l'appeler à nouveau avec exc=NULL pour annuler l'effet
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread_id), None)
            return False

        # Succès
        return True
    
def worker():
    print("start")
    time.sleep(10)
    print("end")

thread = AbortableThread(target=worker, args=())
thread.start()
print("time start")
time.sleep(5)
print("time end")
thread.kill()