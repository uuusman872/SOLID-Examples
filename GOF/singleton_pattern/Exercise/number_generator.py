import threading

class NumberGenerator:
    _instance = None
    _lock = threading.Lock()
    _current_number = 0 

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(NumberGenerator, cls).__new__(cls)
        return cls._instance

    def getNextNumber(self):
        with self._lock:
            number = self._current_number
            self._current_number += 1
            return number
        

if __name__ == "__main__":
    generator1 = NumberGenerator()
    generator2 = NumberGenerator()

    print(f"Generator 1 {generator1.getNextNumber()}")
    print(f"Generator 2 {generator2.getNextNumber()}")
    print(f"Generator 1 {generator1.getNextNumber()}")
    print(f"Generator 2 {generator2.getNextNumber()}")
    print(f"Generator 1 {generator1.getNextNumber()}")
    print(f"Generator 2 {generator2.getNextNumber()}")
    print(f"Generator 1 {generator1.getNextNumber()}")
    print(f"Generator 2 {generator2.getNextNumber()}")
    print(f"Generator 1 {generator1.getNextNumber()}")