class SingletonMeta(type):

    _instance = {}

    def __new__(cls, *args, **kwargs):
        print("ini <super>...")
        new_class = super().__new__(cls, *args, **kwargs)
        cls._instance[new_class] = super(SingletonMeta, new_class).__call__()
        return new_class

    def call(cls, *args, **kwargs):
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
