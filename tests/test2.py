import time
import multiprocessing
from threading import Thread

def func1():
    i = 0
    while i < 100:
        print("Exec")

        time.sleep(3)

if __name__ == '__main__':

    thread1 = multiprocessing.Process(target=func1, args=())

    thread1.start()
    time.sleep(10)
    print("we")
    thread1.terminate()

    print("end")