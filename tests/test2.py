import time
import multiprocessing

def func1():
    i = 0
    while i < 100:
        print("Exec")

        time.sleep(3)

if __name__ == '__main__':
    lock = multiprocessing.Lock()
    text = multiprocessing.Value()
    thread: multiprocessing.Process = multiprocessing.Process(target=func1, args=())
    thread
    thread.start()

    time.sleep(5)
    print("we")
    time.sleep(5)
    thread.terminate()

    print("end")