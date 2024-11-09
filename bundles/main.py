from models.student import Student
from models.proffesor import Proffesor
person_1= Student(
    name = 'Luis',
    lastname = 'Diaz',
    age = 25,
    code = 123456
    )

print(person_1.sayHello())

proffesor_1 = Proffesor(
    name = 'James',
    lastname = 'Rodriguez',
    age = 33
)

print(proffesor_1.sayHello())