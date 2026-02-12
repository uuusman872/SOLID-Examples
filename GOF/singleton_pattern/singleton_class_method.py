class Singleton():

    _instance = None

    def __init__(self):
        raise RuntimeError("Call instance() instead")
    
    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = cls.__new__(cls)

        return cls._instance

    def __str__(self):
        return "This is a constructor singleton"


s1 = Singleton.get_instance()
s2 = Singleton.get_instance()


print(s1 is s2)