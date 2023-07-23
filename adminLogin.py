from tkinter import *
from adminHomePage import adminHomePage
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
        cursor.execute("SELECT id, password FROM admin WHERE id=%s AND password=%s",
                       (userID, userPassword))
        user = cursor.fetchone()

        if user is not None:
            message.set("Login Successful!")
            loginWindow.destroy()
            root = Tk()
            facultyDashboard = adminHomePage(root)
            root.mainloop()

        else:
            message.set("Invalid username or password")


def loginForm():
    global loginWindow
    loginWindow = Tk()
    loginWindow.geometry("350x300")
    loginWindow.title("Admin Login")
    loginWindow.eval('tk::PlaceWindow . center')

    global message
    global name
    global password

    name = StringVar()
    password = StringVar()
    message = StringVar()

    image = PhotoImage(file="imgs/adminLogo.png")
    image_label = Label(loginWindow, image=image)
    image_label.place(x=120, y=30)

    Label(loginWindow, width='300', text='Login with your credentials', font=('Arial', 12), bg="orange",
          fg="white").pack()

    Label(loginWindow, text="Admin ID : ", font=('Arial', 12)).place(x=20, y=140)
    Entry(loginWindow, textvariable=name, font=('Arial', 12)).place(x=110, y=142)

    Label(loginWindow, text='Password : ', font=('Arial', 12)).place(x=20, y=180)
    Entry(loginWindow, textvariable=password, show="*", font=('Arial', 12)).place(x=110, y=182)

    Label(loginWindow, text="", textvariable=message).place(x=115, y=215)
    Button(loginWindow, text="Login", width=10, font=('Arial', 13), height=1, bg="orange", command=login).place(x=130,
                                                                                                                y=245)


    loginWindow.mainloop()


loginForm()
