#t/user/bin/python
#########################
#      Dictionaries
#      Name : David Spencer
#      Date : 23/6/2022
########################
#Initialising dictionaries

Student = {"Name":"Bob","age":18,"gender":"male"} 
Student["Id_number"]= "123345456"
Student["Hobbies"]="Music,druming"
Student["Favourite meal"]= "pizza"
print(Student)
print(Student["Name"])
print(Student["age"])
print(Student["gender"])
print(Student["Id_number"])
print(Student["Hobbies"])
print(Student["Favourite meal"])
#Initilasing an empty dictionary
#variable={}(calibracet)
Student={}
Student["home_city"]="Ngong"
Student["prefferred_sport"]="baskestball"
Student["Name"]="Tom "
print(Student)
del Student["Name"]
print(Student)