#square of number
def get_power(number,power):
    power_number=number**power
    return power_number
print(get_power(6,4))    

def get_full_name(f_name,s_name):
    full_name= f_name + "" + s_name
    return full_name.title()
print(get_full_name('david','spencer'))    

#parsing a list in function
def greet_friends(names):
    for name in names:
        msg= "Hello " + name.title() + "!"
        print (msg)
friends=['tom','mike','ben']        
greet_friends(friends)