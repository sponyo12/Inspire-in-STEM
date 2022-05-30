# how to find divisibility
num =int(input("enter number"))
x =int(input("enter number"))
y=int(input("enter number"))
if (num%x==0) and (num%y==0):
    print(f"the number {num} is divisile by {x} or {y}")
elif(num%x==0) and not(num%y==0):
     print(f"the number {num} is divisile by {x} and not {y}")
elif(num%y==0) and not (num%x==0):
     print(f"the number {num} is divisile by {y} and not {x}")     
else:
    print(f"the number {num} is not divisible by both {x} or {y}")




