# Ad hoc polymorphism: defining a single function that does different things depending on parameters/data types
def add(a, b):
    if isinstance(a, int):
        return a + b
    else:
        return a + " " + b

print(add(1,2))
print(add("Matthew","Bevins"))
# Parametric polymorphism: defining a single function that does the same thing regardless of data types
from typing import TypeVar, List
T = TypeVar('T')
def printItems(items: List[T]) -> None:
    for i in items:
        print(i)
printItems([1,2,3])
printItems(['a','b','c'])

# Subtype polymorphism: defining a parent class with a particular function that can be redefined yet called in the same way by different child classes
class Person:
    def catchphrase(self):
        print("Hello")
class Matthew(Person):
    def catchphrase(self):
        print("Muy Epico")
M = Matthew()
P = Person()
P.catchphrase()
M.catchphrase()