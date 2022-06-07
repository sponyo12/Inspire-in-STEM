class User:
    def __init__(self,_name,_email,_phoneNo):
        self.name=_name
        self.email=_email
        self.phoneNo=_phoneNo
    def sayHi(self):
        print(f"{self.name} is this your email {self.email} and is this your phone number {self.phoneNo}?")
person1=User('David','davidspec580@gmail.com',792879778)
person1.sayHi()


from random import random

print ("WELCOME TO OUR PASSWORD GENERATOR")
num_passwords=int(input("how many passwords would you like to have?"))
length_password =int(input("how many characters will they contain?"))
print("Here are you passwords:")
for password in range(num_passwords):
    password=''
    for characters in range(length_password):
        password += random.choice(characters)
    print(password)

