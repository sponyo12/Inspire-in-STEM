#pyramid of stars
print("\t\t\t*\t\t\t")
print("\t\t*\t*\t*\t\t")
print("\t*\t*\t*\t*\t*\t")
print("*\t*\t*\t*\t*\t*\t*\t")

print("\n")
#diamond of stars
print("\t\t\t*\t\t\t")
print("\t\t*\t*\t*\t\t")
print("\t*\t*\t*\t*\t*\t")
print("*\t*\t*\t*\t*\t*\t*\t")
print("\t*\t*\t*\t*\t*\t")
print("\t\t*\t*\t*\t\t")
print("\t\t\t*\t\t\t")

#pyramid of stars
for R in range (1,11):
    for C in range(11-R):
        print("",end = "")
    for C in range(1,R):
        print("*",end = "")
    for R in range(R, 0, -1):
        print("*",end = "")    

print("\n")        
