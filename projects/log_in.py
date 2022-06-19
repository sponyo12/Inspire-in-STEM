from tkinter import *

def register ():
    screen1=Toplevel
    screen1.title("register")
    screen1.geometry("300x250")

    username=StringVar()
    password=StringVar()
    Label(screen1, text="username *").pack()
    Entry(screen1, textvariable=username)
    Label(screen1, text="password *").pack()
    Entry(screen1, textvariable=password)
def log_in():
    print("beggining login process")

def main_screen ():
    global screen
    screen=Tk()
    screen.geometry("300x250")
    screen.title("Central vallley chats")
    Label(text = "Central vallley chats",bg="grey",width="300",height="2",font=("Calibri",13))
    Label(text="").pack()
    Button(text="LOG IN",width="30",height="2",command= log_in).pack()
    Label(text="").pack()
    Button(text="REGISTER",width="30",height="2",command=register).pack()

    screen.mainloop()
main_screen()    