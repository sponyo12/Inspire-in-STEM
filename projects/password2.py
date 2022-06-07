import random


class User:
    def __init__(self,_name,_email,_phoneNo):
        self.name=_name
        self.email=_email
        self.phoneNo=_phoneNo
    def sayHi(self):
        print(f"{self.name} is this your email {self.email} and is this your phone number {self.phoneNo}?")
person1=User('David','davidspec580@gmail.com',792879778)
person1.sayHi()
user=input("yes or no ?")

if user =="yes":
    print ("WELCOME TO OUR PASSWORD GENERATOR")
    