#mutable:
         #can be edited
         #list[]
         #dictionary{}
#imutable:
          #can't be edited
         #tuples()

#list
fruits=['mango','guava','banana','lime']
fruits[2]='apple'
#print(fruits)

#tuples
new_fruits=('mango','guava','banana','lime')
#print(new_fruits[2])
#new_fruits[1]='apple'
#print(new_fruits)



cars=('audi','bmw','vw','toyota')
cars=('nissan','bmw','vw','toyota')
#print(cars)

fav_foods=('pizza','kfc','chapati','rice','kuku')
for fav_food in fav_foods:
    print(fav_food)