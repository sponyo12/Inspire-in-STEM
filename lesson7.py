#Learning about list
from pydoc import plain

motocycle_owner = "David Spencer"
plate_number=[' H123\n',' S456\n',' Y789']
motocycle = ['Honda','Suzuki','Yamaha']
#accessing list items using index
#print(motocycle)
#print(motocycle[0])
#print("I love " + str (motocycle[1]))

#changing ellement's in a list
#motocycle[0]= 'Bugati' 
#print(motocycle)
#motocycle[1]= 'Bugati'
#print(motocycle)

#adding ellements in a list
#motocycle.append("Bugati")
#print(motocycle)

#print(motocycle[0]  + plate_number[0],motocycle[1] + plate_number[1],motocycle[2] + plate_number[2])

#Deleting an item from a list --del
#del motocycle[0]
#del motocycle[1]
#del motocycle[2]
#print(motocycle)

#Deleting an item from a list --popped method
#popped_motocycle = motocycle.pop()
#print (popped_motocycle)

#My name is David spencer and I own a motocycle plate_number h123
#print(f"My name is {motocycle_owner} and I owna {motocycle[1]} motocycle{plate_number[1]}") 
#statement = (f"My name is {motocycle_owner} and I owna {motocycle[1]} motocycle{plate_number[1]}") 
#print(statement)

#Removing an item from a list --remove
motocycle.remove ("Honda")
print(motocycle)