class Person:
    def __init__(self,_name,_age):
        self.name=_name
        self.age=_age
    def sayHi(self):
        print(f"Hello,my name is {self.name} and I'm {self.age} years old")    
person1=Person('David',16)        