from tkinter import *
from facultyHomePage import facultyHomePage
import mysql.connector

connection = mysql.connector.connect(
    user='root',
    password='sureshchoudhary',
    host='localhost',
    database='stdmng'
)

loginWindow = None

def login():
    global loginWindow
    userID = name.get()
    userPassword = password.get()

    if(userID == '' or userPassword == ''):
        message.set('Please fill all the fields')
    else:
        cursor = connection.cursor()
        cursor.execute("SELECT id, password FROM faculties WHERE id=%s AND password=%s",
                       (userID, userPassword))
        user = cursor.fetchone()


        if user is not None:
            message.set("Login Successful!")
            loginWindow.destroy()
            root = Tk()
            welcome_page = facultyHomePage(root,user[0])
            root.mainloop()

        else:
            message.set("Invalid username or password")


def loginForm():
    global loginWindow
    loginWindow = Tk()
    loginWindow.geometry("350x300")
    loginWindow.title("Faculty Login")
    loginWindow.eval('tk::PlaceWindow . center')

    global message
    global name
    global password

    name = StringVar()
    password = StringVar()
    message = StringVar()

    image = PhotoImage(file="imgs/facultyLogo.png")
    image_label = Label(loginWindow, image=image)
    image_label.place(x=145, y=30)

    Label(loginWindow, width='300', text='Login with your credentials', font=('Arial', 12), bg="orange",
          fg="white").pack()

    Label(loginWindow, text="Faculty ID : ", font=('Arial', 12)).place(x=20, y=120)
    Entry(loginWindow, textvariable=name, font=('Arial', 12)).place(x=110, y=122)

    Label(loginWindow, text='Password : ', font=('Arial', 12)).place(x=20, y=160)
    Entry(loginWindow, textvariable=password, show="*", font=('Arial', 12)).place(x=110, y=162)

    Label(loginWindow, text="", textvariable=message).place(x=115, y=200)
    Button(loginWindow, text="Login", width=10, font=('Arial', 13), height=1, bg="orange", command=login).place(x=130,
                                                                                                                y=230)

    loginWindow.mainloop()


loginForm()
