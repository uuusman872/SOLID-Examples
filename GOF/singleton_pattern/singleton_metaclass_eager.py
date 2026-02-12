class SingletonMeta(type):

    _instance = {}

    def __init__(cls, name, base, dict):
        super().__init__(name, base, dict)
        cls._instance[cls] = super().__call__()
        print("ini <super>...")
    
    def __call__(cls, *args, **kwds):
        return cls._instance[cls]


class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        print("init <child> ...")
        self.attribute = "i'm a singleton"

# s1 = Singleton()
# s2 = Singleton()

# print(s1.attribute)
# print(s2.attribute)

# print(s1 is s2)
