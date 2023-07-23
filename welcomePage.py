from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
from _tkinter import *
from tkinter import Tk, Label
from PIL import ImageTk, Image
import os


class WelcomePageClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.resizable(False, False)

        # background
        image = Image.open("imgs/wallpaper.jpg")
        image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
        self.background_image = ImageTk.PhotoImage(image)

        self.background_label = Label(root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        window_height = 500
        window_width = 800
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))
        self.root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))

        self.body()

    def body(self):
        self.heading = tk.Label(root, text="Welcome to our Student Management System App", font=("Arial", 20,"bold"),width=300,foreground='white',background='blue',pady=15)
        self.heading.pack()

        self.image = tk.PhotoImage(file="imgs/mruLOGO.png")
        self.image_label = tk.Label(root, image=self.image)
        self.image_label.place(x=120, y=150)



        self.login_button1 = tk.Button(
            self.root,
            text="Student Login",
            command=self.run_student_file,
            font=('Arial', 15),
            foreground='white',
            background='#ff4f00',
            activebackground="#f98129",
            activeforeground="white",
            padx=3,
            pady=3,
            relief=RAISED,
            borderwidth=6
        )
        self.login_button1.place(x=480,y=150)

        self.login_button2 = tk.Button(
            self.root,
            text="Faculty Login",
            command=self.run_faculty_file,
            font=('Arial', 15),
            foreground='white',
            background='#ff4f00',
            activebackground="#f98129",
            activeforeground="white",
            padx=3,
            pady=3,
            relief=RAISED,
            borderwidth=6
        )
        self.login_button2.place(x=480,y=230)

        self.login_button3 = tk.Button(
            self.root,
            text="Admin Login",
            command=self.run_admin_file,
            font=('Arial', 15),
            foreground='white',
            background='#ff4f00',
            activebackground="#ff4f09",
            activeforeground="white",
            padx=3,
            pady=3,
            relief=RAISED,
            borderwidth=6
        )
        self.login_button3.place(x=485,y=310)
    def run_student_file(self):
        root.destroy()
        os.system("python studentLogin.py")

    def run_faculty_file(self):
        root.destroy()
        os.system("python facultyLogin.py")

    def run_admin_file(self):
        root.destroy()
        os.system("python adminLogin.py")


if __name__ == "__main__":
    root = tk.Tk()
    welcome_page = WelcomePageClass(root)
    root.mainloop()
