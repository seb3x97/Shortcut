import threading
import time
import ctypes


class thread_with_exception(threading.Thread):
    def __init__(self, name, *args, **keywords):
        threading.Thread.__init__(self, *args, **keywords)
        self.name = name
    
    """
    def run(self):
 
        # target function of the thread class
        try:
            while True:
                print('running ' + self.name)
                for i in range(100000000000):
                    print(str(i))
                #time.sleep(20)
        finally:
            print('ended')
    """

    def init(self):
        print (self.ident)
        print (self.native_id)
        print (self.get_id())
          
    def get_id(self):
        # Check si le thread est démarré
        if not self.is_alive: return None

        #return self.ident

        # returns id of the respective thread
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id
  
    def raise_exception(self) -> bool:
        # On essaye de récupérer l'identifiant du thread
        thread_id = self.get_id()
        if thread_id is None: return False

        # On essaye de fermer le thread
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread_id), ctypes.py_object(SystemExit))
        if res > 1: res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread_id), 0)
        if res > 1: return False

        # Succès
        return True

def worker():
    for i in range(100000000000):
        #pass
        print(str(i))

thread = thread_with_exception('Thread 1', target=worker, args=())
thread.start()
#thread.init()
#thread.start()
time.sleep(2)
thread.raise_exception()
#thread.join()