#the n terms in an AP
a = int(input("Enter the value of a: "))
d = int(input("Enter the value of d: "))
n = int(input("Enter the value of n: "))
 
# 2. Loop for n terms
for i in range(1,n+1):
    n_term = a + (i-1)*d
    print(n_term)
sum_n=(n_term/2)*(2*a+(n-1)*d)
print(sum_n)

#geometric progresion
a = int(input("Enter the value of a: "))
r = int(input("Enter the value of r: "))
n = int(input("Enter the value of n: "))
 
# 2. Loop for n terms
for i in range(1,n+1):
    t_n = a * r**(i-1)
    print(t_n)



























