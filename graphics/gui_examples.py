#t/user/bin/python
#########################
#      graphical interface
#      Name : David Spencer
#      Date : 7/6/2022
########################



from tkinter import *
from tkinter import font
window =Tk()
window.title("welcome to my app.")
window.geometry("700x600")
window.configure(bg='navy')
lbl=Label(window,text="Welcome to my app ",font=("Arial ",20))
f_name=Label(window,text="First name",font=("Arial ",20))
s_name=Label(window,text="Second name",font=("Arial ",20))

lbl.grid(column=60,row=100)
f_name.grid(column=60,row=160)
s_name.grid(column=60,row=170)

def open_pop_up():
    top=Toplevel(window)
    top.geometry("300x300")
    top.title("Pop up window")
    top.configure(bg="green")
    msg=Label(top,text="Welcome to pop up",font=("Mistral", 18))

btn=Button(window,text="sign up",bg="lavender",fg="black",)
btn.grid(column=100,row=150)

f_name_box=Entry(window,width=20)
f_name_box.grid(column=100,row=160)
s_name_box=Entry(window,width=20)
s_name_box.grid(column=100,row=170)






window.mainloop()
















