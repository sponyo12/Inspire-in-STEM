#t/user/bin/python
#########################
#      Dictionaries
#      Name : David Spencer
#      Date : 31/5/2022
########################
#python functions

#what is a functions?=this is a block of code that gets executed together
#initialisins fuctions
#calling functions
def say_hello():
    print('Hello from JKUAT')
    x=4
    y=7
    z=x+y
    print(z)
say_hello()  #calling functions
def bark():
    print('Dogs bark wooof woof')
bark()    #calling functions
def moo():    
    print('cow goes mooo')
moo()    #calling functions    
def meow():
    print('cat goes meow')
meow()    #calling functions
#sum of number
def add_numbers(a,b):
    sum_numbers=a+b
    print("the sum of numbers:",sum_numbers)
add_numbers(40,50)
add_numbers(10,30)
add_numbers(400,500)
#product of number
def add_numbers(a,b):
    prod_numbers=a*b
    print("the product of numbers:",prod_numbers)
add_numbers(40,50)
add_numbers(10,30)
add_numbers(400,500)


#using default parameters
def print_name (name="David spencer"):
    print(name)
print_name("Thomas")    
#return from a function
def get_sum(num_1,num_2):
    sum_num=num_1+num_2
    return sum_num
print(get_sum(7,12))     

