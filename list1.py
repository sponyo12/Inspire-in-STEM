#t/user/bin/python
#########################
#      For loops for lists
#      Name : David Spencer
#      Date : 24/6/2022
########################
#list on squares

squares = []
for number in range(0,10):
    square = number**2
    squares.append(square)
print(squares)

cubes = []
for number in range(0,10):
    cube = number**3
    cubes.append(cube)
print(cubes)    

sum = 0
for numbers in range(0,100):
    sum = sum+numbers
    
print(sum)    