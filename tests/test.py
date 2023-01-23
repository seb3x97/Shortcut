
import multiprocessing
import time


class Test:
    def __init__(self) -> None:
        pass

    def test(self):
        __process: multiprocessing.Process = multiprocessing.Process(target=self.exec_actions, args=())
        __process.start()
        
    def exec_actions(self):
        print("we")


if __name__ == "__main__":
    test = Test()
    test.test()