# data structures:(simply a container storing data in an order)
    #lists =['value','value'] 
    # dictionaries ={'key':'value'}
# what are dictionaries (a collection of key value pairs) 
#syntax for dictionaries ={'Key':'value'}
#define,access,add,remove
#looping over dictinaries
#dictionary in dictonary, list in dictionary, dictionary in list

names =('john','mary')
list_names =['john','mary']
colours ={'colour':'red'}
vehicle ={'type':'toyota','plate_number':'kwz45'}
#print(type(colours))
#print(type(list_names))#we use the type of method 
#acessing values in a dictionary
#print(vehicle)
#print(vehicle['type'])#you can acess the value of an ellement inside a dictionary using the key
#print(vehicle['plate_number'])
#dictionary person
person ={'name':'David Spencer',
         'gender':'male',
         'phone_no':'0792878324'
         ,'location':'Nairobi'}
#print(person)
#print(person['name'])
#print(person['gender'])
#print(type(person))
#print(vehicle['type'],vehicle['plate_number'])
#print(person['name'],person['gender'],person['location'],person['phone_no'])
#adding items into a key dict['key']='value'
person['age']='18'
person['fav_colour']='junlge green'
#print(person)
#print(person['name'],person['age'],person['fav_colour'])
#del (person['phone_no'])
#print(person)
#looping over dictionaries
#for key,value in person.items():
    #print(f"{key}:{value}")
#print (person['gender'])

#Using get to access the value in adictionary
#print(person.get('location','the loction key is non existent'))
print(person.get('password','the loction key is non existent'))