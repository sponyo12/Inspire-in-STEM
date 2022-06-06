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






