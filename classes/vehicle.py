class Vehicle:
    def __init__(self,_mileage,_speed):
        self.mileage=_mileage
        self.speed=_speed
    def sayHi(self):
     print(f"The mileage of the vehicle is {self.mileage} and its speed is {self.speed}.")
toyota=Vehicle(4000,100)            
toyota.sayHi()        
mercedes=Vehicle(40000,180)            
mercedes.sayHi()        

