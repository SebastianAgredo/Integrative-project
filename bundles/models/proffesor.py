from models.person import Person

class Proffesor(Person):
    def __init__(name,lastname,age,bachelor=True):
        super().__init__(name,lasname,age)

    def __str__(self):
        return f"Proffesor(name={self.name},lastname= {self.lastname})"

    
    def sayHello(self):
        return f"Hola soy un profesor y mi nombre es : {self.name}"