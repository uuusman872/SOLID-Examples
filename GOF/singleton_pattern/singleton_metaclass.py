class SingletonMeta(type):
    _instance = {}

    def __call__(cls,  *args, **kwargs):
        print("<call meta> calling... ")
        if cls not in cls._instance:
            instance = super().__call__(*args, **kwargs)
            cls._instance[cls] = instance
        
        return cls._instance[cls]
    


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        print("This is some business logic")

# s1 = Singleton()
# s2 = Singleton()

# print(s1 is s2)