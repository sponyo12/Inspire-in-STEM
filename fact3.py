#customising geetings
#name=input("enter your name")
#print(f"Hello {name}")
from cmd import PROMPT


num=20
num+=num
#print(num)
#num + num = 40
PROMPT="enter your name so that we can customise it"
PROMPT+="\nenter your name:"
print("hello",input(PROMPT))
