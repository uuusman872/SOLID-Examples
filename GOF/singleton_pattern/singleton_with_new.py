

class Singleton:
    _instance = None

    def __new__(cls):
        print("<new> called")
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __str__(self):
        return "This is with new function"

    def __init__(self):
        print("<init> called")


s1 = Singleton()
s2 = Singleton()


print(s1 is s2)