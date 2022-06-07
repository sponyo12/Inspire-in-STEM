from os import name


#t/user/bin/python
#########################
#      Name : David Spencer
#      Date : 6/6/2022
########################
class Student:
    def __init__(self,name,hobby,reg_no,grade):
        self.name=name
        self.hobby=hobby
        self.reg_no=reg_no
        self.grade=grade
    def sayHi(self):
        print(f"my name is {self.name} \n my hobby is {self.hobby} \n my registration number is {self.reg_no} \n my grade is {self.grade}")