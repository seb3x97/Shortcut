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
          
    def get_id(self):
 
        # returns id of the respective thread
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id
  
    def raise_exception(self):
        print("exeption")
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
              ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Exception raise failure')

def worker():
    for i in range(100000000000):
        print(str(i))

thread = thread_with_exception('Thread 1', target=worker, args=())
thread.start()
time.sleep(2)
thread.raise_exception()
#thread.join()