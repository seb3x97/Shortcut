# SuperFastPython.com
# example of using a manager to create a custom class
from time import sleep
from random import random
from multiprocessing import Process
from multiprocessing.managers import BaseManager
 
# custom class
class MyCustomClass():
    # constructor
    def __init__(self):
        # store the data in the instance
        self._name = "test"
        self.element = MyCustomClass()

    def getName(self):
        return self._name
    
    def setName(self, value):
        self._name = value

    def getElement(self):
        return self.element
 
# custom manager to support custom classes
class CustomManager(BaseManager):
    # nothing
    pass
 
# custom function to be executed in a child process
def work(shared_custom):
    # call the function on the shared custom instance
    print(f"before {shared_custom.getName()}")
    
    shared_custom.setName("we")

    # report the value
    print(f"after {shared_custom.getName()}")
 
# protect the entry point
if __name__ == '__main__':
    # register the custom class on the custom manager
    CustomManager.register('MyCustomClass', MyCustomClass)
    # create a new manager instance
    with CustomManager() as manager:
        # create a shared custom class instance
        shared_custom = manager.MyCustomClass()

        # start some child processes
        process = Process(target=work, args=(shared_custom,))
        process.start()
        process.join()

        # all done
        print('Done')

        print(f"end {shared_custom.getElement().getName()}")