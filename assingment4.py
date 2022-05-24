#write a program to withdraw :
#25K if acc_bal is btwn 100K to 200K
#30% if bal is btwn 500K and 1M
#above 1M deduct 15000

from os import access


acc_bal =input("What is your balance?")
if (int(acc_bal)>100000 and int(acc_bal)<200000):
    acc_bal=int(acc_bal)-25000
    print(f"Your account has been deducted 25000. Account balance is{acc_bal}")
elif (int(acc_bal)>500000 and int(acc_bal)<1000000):
        acc_bal=int(acc_bal)- (acc_bal*0.03)
        print(f"You account has been deducted 30%. Account balance is{int(acc_bal)}")
elif (int (acc_bal) >1000000) :
    acc_bal =int(acc_bal)-15000
    print(f"You account has been deducted 15000. Account balance is{int(acc_bal)}")
else:
    print('No money for you')
    