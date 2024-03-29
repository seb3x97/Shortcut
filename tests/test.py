# SuperFastPython.com
# example of using a manager to create a custom class
from time import sleep
from random import random
from multiprocessing import Process
from multiprocessing.managers import BaseManager
from random import randint
 
# custom class
class MyCustomClass():
    # constructor
    def __init__(self, actions):
        self.name = ""
        # store the data in the instance
        self.actions = actions

    def getActions(self):
        return self.actions
    
    def setActions(self, value):
        self.actions = value

    def setName(self, value):
        self.name = value

    def getName(self):
        return self.name
 
# custom manager to support custom classes
class CustomManager(BaseManager):
    # nothing
    pass

class Action:
    def __init__(self) -> None:
        self.name = "test"

    def setName(self, value):
        self.name = value

    def getName(self):
        return self.name
 
# custom function to be executed in a child process
def work(manager):
    # call the function on the shared custom instance
    print(f"before {manager.getName()}")

    for action in manager.getActions():
        action.setName("=> " + str(randint(0, 10000)))

    # report the value
    manager.setName("asdfgasdas")
    print(f"after {manager.getName()}")

    for action in manager.getActions():
        print(action.getName())
 
# protect the entry point
if __name__ == '__main__':
    # register the custom class on the custom manager
    CustomManager.register('MyCustomClass', MyCustomClass)
    # create a new manager instance
    with CustomManager() as manager:
        actions = [Action(), Action(), Action()]
        # create a shared custom class instance
        shared_custom = manager.MyCustomClass(actions)

        # start some child processes
        process = Process(target=work, args=(shared_custom,))
        process.start()
        process.join()

        # all done
        print('Done')

        for action in shared_custom.getActions():
            print(action.getName())