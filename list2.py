 
#list of vehicles
vehicles_name = ['bmw','audi','toyota','mercedes','jeep']
vehicle = input("What is your vehicles name ?")
#using a for loop to print vehicle
for vehicle in vehicles_name:
    if vehicle == vehicles_name[4]:
        print(vehicle.upper())
    #print(vehicle.title())
    