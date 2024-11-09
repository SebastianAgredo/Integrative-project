from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    @abstractmethod
    def sayHello(self):
        pass
