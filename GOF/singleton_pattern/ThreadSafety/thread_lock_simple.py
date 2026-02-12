from threading import Thread
from threading import Lock

class Counter:
    def __init__(self):
        self.count = 0
        self.lock = Lock()
    
    def increment(self):
        self.lock.acquire()
        self.count += 1
        self.lock.release()

    