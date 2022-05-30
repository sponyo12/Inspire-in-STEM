#Write a program that gets user input thata adds ksh 10,000 to their acount if she is btwn 25-30 yrs
age =input("What is your age?")
gender =input("What gender are you: male/female?")
name =input("user name")
accout_balance =0

if (int (age) > 25) and (int(age) < 30 ) :
    accout_balance = accout_balance +10000
    print("You have recieved Ksh 10000")
else:
    print("Sorry no money for you")    

