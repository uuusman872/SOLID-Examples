import threading


class ThreadSafeSingleton(type):
    _lock = threading.Lock()
    _instance = {}
    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instance:
                cls._instance[cls] = super().__call__(*args, **kwargs)
            return cls._instance
    

class Singleton(metaclass=ThreadSafeSingleton):
    def __init__(self):
        pass


def get_singleton_instance():
    s = Singleton()
    print(s)


threads = []
for i in range(10):
    t = threading.Thread(target=get_singleton_instance)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()
