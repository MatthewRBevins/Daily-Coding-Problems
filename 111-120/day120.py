class node:
    def __init__(self, value):
        self.value = value
global instance 
instance = None
global instance2 
instance2 = None
global curCall 
curCall = 0
class Singleton:
    def __init__(self, val):
        global instance
        global instance2
        if instance == None:
            instance = node(val)
        elif instance2 == None:
            instance2 = node(val)
    def getInstance():
        global curCall
        if curCall == 0:
            curCall = 1
            return instance2
        else:
            curCall = 0
            return instance

# Example usage:
instance1 = Singleton(1)
instance2 = Singleton(2)
print(Singleton.getInstance())
print(Singleton.getInstance())