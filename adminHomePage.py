import tkinter as tk
from tkinter import *
import os
from tkinter import Tk, Label
from PIL import ImageTk, Image

class adminHomePage:
    def __init__(self, root):
        self.root = root

        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.root.geometry("%dx%d" % (self.width, self.height))
        self.root.title("Student management system")

        # background
        image = Image.open("imgs/wallpaper2.jpg")
        image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.Resampling.LANCZOS)
        self.background_image = ImageTk.PhotoImage(image)
        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.body()

    def body(self):
        self.label = tk.Label(self.root, text="ADMIN DASHBOARD",
                              font=("Arial", 38, 'underline'))
        self.label.pack(pady=10)

        self.label = tk.Label(self.root, text="Malla Reddy University", font=("Arial", 28))
        self.label.pack(pady=10)

        # ------ student --------

        self.image = tk.PhotoImage(file="imgs/studentLogo.png",height=100,width=100)
        self.button1 = tk.Button(self.root, text="Student data",width=250, compound=tk.TOP, font=('Arial', 20),
                                 image=self.image, command=self.student,relief=RAISED,borderwidth=7,background='orange')
        self.button1.place(x=100, y=200)

        # ---- faculty button----

        self.image2 = tk.PhotoImage(file="imgs/teacherImg.png")
        self.button2 = tk.Button(self.root, text="Faculty data",width=230, compound=tk.TOP, font=('Arial', 20), image=self.image2,
                                 command=self.faculty, relief=RAISED,padx=20,borderwidth=7,background='orange')
        self.button2.place(x=450, y=200)

        # ---- student attendance button----

        self.image3 = tk.PhotoImage(file="imgs/attendanceImg.png")
        self.button3 = tk.Button(self.root, text="Student Attendance", compound=tk.TOP, font=('Arial', 20),
                                 image=self.image3,
                                 command=self.attendance,
                                 relief=RAISED,
                                 borderwidth=7,
                                 background='orange')
        self.button3.place(x=805, y=200)

        self.image5 = tk.PhotoImage(file="imgs/book.png", height=96)
        self.button5 = tk.Button(self.root, text="Manage Subjects",width=250, compound=tk.TOP, font=('Arial', 20),
                                 image=self.image5,
                                 command=self.manageSubjects,
                                 relief=RAISED,
                                 borderwidth=7,
                                 background='orange')
        self.button5.place(x=100, y=450)

        # ---- send notification/mails button----

        self.image6 = tk.PhotoImage(file="imgs/chat.png", height=96)
        self.button6 = tk.Button(self.root, text="Manage messages",width=260, compound=tk.TOP, font=('Arial', 20),
                                 image=self.image6,
                                 command=self.adminNotification,
                                 relief=RAISED,
                                 borderwidth=7,
                                 background='orange')
        self.button6.place(x=450, y=450)


        #----- logout button -----
        self.logoutImg = tk.PhotoImage(file="imgs/logout.png")
        self.logoutBtn = tk.Button(
            self.root,
            text="Logout",
            image=self.logoutImg,
            compound=tk.LEFT,
            font=('Arial',15,"bold"),
            command=self.logoutAdmin,
            relief=RAISED,
            borderwidth=7,
            background='pink'
        )
        self.logoutBtn.place(x=1350, y=700)


    def student(self):
        self.root.destroy()
        os.system("python studentMng.py")

    def faculty(self):
        self.root.destroy()
        os.system("python facultyMng.py")
    def logoutAdmin(self):
        self.root.destroy()
        os.system("python welcomePage.py")
    def attendance(self):
        os.system("python studentAttendance.py")
    def manageSubjects(self):
        os.system("python manageCourse.py")

    def adminNotification(self):
        os.system("python adminNotification.py")


if __name__ == "__main__":
    root = tk.Tk()
    welcome_page = adminHomePage(root)
    root.mainloop()
