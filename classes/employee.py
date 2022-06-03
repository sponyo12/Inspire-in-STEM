class Employee:
    def __init__(self,_name,_salary):
        self.name=_name
        self.salary=_salary
    def sayHi(self):
        print(f"i am {self.name} and my salary is {self.salary} ") 
employee1=Employee('Tom',200000)
employee1.sayHi()
employee2=Employee('Kevin',200000)          
employee2.sayHi()