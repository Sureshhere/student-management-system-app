import tkinter as tk


class HomePage:
    def __init__(self, root):
        self.root = root

        # Setting tkinter window size
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.root.geometry("%dx%d" % (self.width, self.height))
        self.root.title("Student management system")
        self.root.config(bg='lavender')
        self.body()


    def body(self):
        self.label = tk.Label(self.root, text="Welcome to the Student Management System App!",
                              font=("Arial", 38, 'underline'))
        self.label.pack(pady=10)

        self.label = tk.Label(self.root, text="Malla Reddy University", font=("Arial", 28))
        self.label.pack(pady=10)

        # ------ OPTIONS MENU --------

        self.image = tk.PhotoImage(file="profile.png")
        self.button1 = tk.Button(self.root, text="Student Profile", compound=tk.TOP, font=('Arial', 20),
                                 image=self.image, command=self.student)
        self.button1.place(x=120, y=200)

        # ---- Attendance button----

        self.image2 = tk.PhotoImage(file="attendanceImg.png")
        self.button2 = tk.Button(self.root, text="Attendance", compound=tk.TOP, font=('Arial', 20), image=self.image2,
                                 command=self.attendance, padx=20)
        self.button2.place(x=420, y=200)



    def student(self):
        print("student profile clicked!")

    def attendance(self):
        print("attendance clicked!")



if __name__ == "__main__":
    root = tk.Tk()
    welcome_page = HomePage(root)
    root.mainloop()
