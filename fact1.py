import math
def fact(n):
    return(math.factorial(6))
#num =int(input("enter the number:"))    
#f =fact(num)
#print("factorial of ",num,"is", f)

number =int(input("enter the number"))
factorial= 1
if number < 0:
    print("factorial of negative number does not exist")
elif number==0:
    print("factorial of 0 is 1" )
else:    
   for i in range(1,number + 1):    
       factorial = factorial*i    
   print("The factorial of",number,"is",factorial) 

   
     