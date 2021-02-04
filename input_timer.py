import time
from threading import Thread
import sys

answer = None


def check():
    time.sleep(2)
    if answer is None:
        print("Too Slow")
        print("Goodbye"), sys.exit()


    else:
        return


Thread(target=check).start()

answer = input("Input something: ")
