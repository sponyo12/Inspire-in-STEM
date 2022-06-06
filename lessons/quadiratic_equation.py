#t/user/bin/python
#########################
#      Dictionaries
#      Name : David Spencer
#      Date : 31/5/2022
########################
# solving quadiratic equations
from cmath import sqrt
import math
a=int(input("enter the cofficient of the first term (a):"))
b=int(input("enter the cofficient of the second term (b):"))
c=int(input("enter the constant term (c):"))
w= math.sqrt((b**2)-(4*a*c))

def find_roots(a,b,c):
    y_1=(-b+(w))/(2*a)
    y_2=(+b-(w))/(2*a)
    print("the roots of the quadiratic equation are:",y_1,y_2)
find_roots(a,b,c)    