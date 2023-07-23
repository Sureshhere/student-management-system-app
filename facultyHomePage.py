import tkinter as tk
from tkinter import *
from tkinter import messagebox,ttk,Tk,Label
import os
from PIL import ImageTk, Image
import mysql.connector
import webview

class facultyHomePage:
    def __init__(self, root,id="F001"):
        self.root = root
        self.id = id
        self.connection = mysql.connector.connect(
            user='root',
            password='sureshchoudhary',
            host='localhost',
            database='stdmng'
        )

        # Setting tkinter window size
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
        self.lbl_id = tk.Label(self.root,text="Account: "+str(self.id),font=("Arial", 18),background='#000338',foreground="white")
        self.lbl_id.place(x=10,y=10)

        self.label = tk.Label(self.root, text="FACULTY DASHBOARD",
                              font=("Arial", 38, 'underline'))
        self.label.pack(pady=10)

        self.label = tk.Label(self.root, text="Malla Reddy University", font=("Arial", 28))
        self.label.pack(pady=10)

        # ------ profile --------

        self.image = tk.PhotoImage(file="imgs/profile2.png",height=100,width=100)
        self.button1 = tk.Button(self.root, text="Profile",width=250, compound=tk.TOP, font=('Arial', 20),
                                 image=self.image, command=self.view_profile,relief=RAISED,borderwidth=7,background='orange')
        self.button1.place(x=100, y=200)

        self.image2 = tk.PhotoImage(file="imgs/bar-chart-100.png", height=100, width=100)
        self.button2 = tk.Button(self.root, text="Exam Marks Analysis", width=250, compound=tk.TOP, font=('Arial', 20),
                                 image=self.image2, command=self.getStdMarksReport, relief=RAISED, borderwidth=7,
                                 background='orange',padx=10)
        self.button2.place(x=450, y=200)



        self.image3 = tk.PhotoImage(file="imgs/attendanceImg.png")
        self.button3 = tk.Button(self.root, text="Student Attendance", compound=tk.TOP, font=('Arial', 20),
                                 image=self.image3,
                                 command=self.attendance,
                                 relief=RAISED,
                                 borderwidth=7,
                                 background='orange')
        self.button3.place(x=805, y=200)

        # ---- subjects button----

        self.image5 = tk.PhotoImage(file="imgs/leave.png", height=96)
        self.button5 = tk.Button(self.root, text="Apply for a leave",width=250, compound=tk.TOP, font=('Arial', 20),
                                 image=self.image5,
                                 command=self.applyLeave,
                                 relief=RAISED,
                                 borderwidth=7,
                                 background='orange')
        self.button5.place(x=100, y=450)

        # ---- send notification/mails button----

        self.image6 = tk.PhotoImage(file="imgs/chat.png", height=96)
        self.button6 = tk.Button(self.root, text="Send Notifications",width=260, compound=tk.TOP, font=('Arial', 20),
                                 image=self.image6,
                                 command=self.facultyNotification,
                                 relief=RAISED,
                                 borderwidth=7,
                                 background='orange')
        self.button6.place(x=450, y=450)





        # ----- logout button -----
        self.logoutImg = tk.PhotoImage(file="imgs/logout.png")
        self.logoutBtn = tk.Button(
            self.root,
            text="Logout",
            image=self.logoutImg,
            compound=tk.LEFT,
            font=('Arial', 15, "bold"),
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

    def applyLeave(self):
        webview.create_window('Apply for a leave', 'website/facultyapplyleave.html',height=900)
        webview.start()

    def getStdMarksReport(self):
        os.system("python studentMarksAnalysis.py")

    def facultyNotification(self):
        os.system("python facultyNotification.py")

    def get_student_profile(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM faculties WHERE id=%s", (id,))
            student_data = cursor.fetchone()
            return student_data
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Error fetching student profile: {error}")
            return None

    def view_profile(self):
        id = self.id
        student_data = self.get_student_profile(id)
        if student_data:
            profile_window = tk.Toplevel(self.root)
            profile_window.title("Student Profile")
            profile_window.geometry("400x300")

            # Create a treeview widget
            tree = ttk.Treeview(profile_window)
            tree.pack(expand=True, fill='both')

            # Define columns
            tree["columns"] = ("attribute", "value")
            tree.column("#0", width=0, stretch=tk.NO)
            tree.column("attribute", anchor=tk.W, width=150)
            tree.column("value", anchor=tk.W, width=250)

            # Add column headings
            tree.heading("attribute", text="Attribute")
            tree.heading("value", text="Value")

            # Add student profile data to the treeview
            tree.insert("", tk.END, text="", values=("ID", student_data[0]))
            tree.insert("", tk.END, text="", values=("Name", student_data[1]))
            tree.insert("", tk.END, text="", values=("Subject", student_data[2]))
            # tree.insert("", tk.END, text="", values=("Password", '********'))  # Remove this line
            tree.insert("", tk.END, text="", values=("Email", student_data[4]))
            tree.insert("", tk.END, text="", values=("Gender", student_data[5]))
            tree.insert("", tk.END, text="", values=("Contact", student_data[6]))
            tree.insert("", tk.END, text="", values=("DOB", student_data[7]))
            tree.insert("", tk.END, text="", values=("Experience", student_data[8]))

            edit_button = tk.Button(profile_window, text="Edit",
                                    command=lambda: self.edit_profile(profile_window, student_data))
            edit_button.pack(pady=10)
        else:
            messagebox.showerror("Error", "Failed to fetch student profile")

    def edit_profile(self, profile_window, student_data):
        edit_window = tk.Toplevel(profile_window)
        edit_window.title("Edit Profile")
        edit_window.geometry("400x500")

        # Create entry fields for each student attribute
        id_label = Label(edit_window, text="ID :", font=('Arial', 13))
        id_entry = Entry(edit_window, font=('arial', 13))
        id_label.pack()
        id_entry.pack()

        name_label = Label(edit_window, text="Name:", font=('Arial', 13))
        name_entry = Entry(edit_window, font=('arial', 13))
        name_label.pack()
        name_entry.pack()

        subject_label = Label(edit_window, text="Subject:", font=('Arial', 13))
        subject_entry = Entry(edit_window, font=('arial', 13))
        subject_label.pack()
        subject_entry.pack()

        email_label = Label(edit_window, text="Email:", font=('Arial', 13))
        email_entry = Entry(edit_window, font=('arial', 13))
        email_label.pack()
        email_entry.pack()

        gender_label = Label(edit_window, text="Gender:", font=('Arial', 13))
        gender_entry = Entry(edit_window, font=('arial', 13))
        gender_label.pack()
        gender_entry.pack()

        contact_label = Label(edit_window, text="Contact:", font=('Arial', 13))
        contact_entry = Entry(edit_window, font=('arial', 13))
        contact_label.pack()
        contact_entry.pack()

        dob_label = Label(edit_window, text="DOB:", font=('Arial', 13))
        dob_entry = Entry(edit_window, font=('arial', 13))
        dob_label.pack()
        dob_entry.pack()

        experience_label = Label(edit_window, text="Experience:", font=('Arial', 13))
        experience_entry = Entry(edit_window, font=('arial', 13),width=25)
        experience_label.pack()
        experience_entry.pack()

        id_entry.insert(0, student_data[0])
        name_entry.insert(0, student_data[1])
        subject_entry.insert(0, student_data[2])
        email_entry.insert(0, student_data[4])
        gender_entry.insert(0, student_data[5])
        contact_entry.insert(0, student_data[6])
        dob_entry.insert(0, student_data[7])
        experience_entry.insert(0, student_data[8])

        def save_profile():
            new_id = id_entry.get()
            new_name = name_entry.get()
            new_subject = subject_entry.get()
            new_email = email_entry.get()
            new_gender = gender_entry.get()
            new_contact = contact_entry.get()
            new_dob = dob_entry.get()
            new_experience = experience_entry.get()

            updated_data = (
            new_id, new_name, new_subject, new_email, new_gender, new_contact, new_dob, new_experience)
            self.update_student_profile(updated_data)


            messagebox.showinfo("Success", "Profile updated successfully")


            edit_window.destroy()
            profile_window.destroy()

        save_button = Button(edit_window, text="Save", command=save_profile)
        save_button.pack(pady=10)

    def update_student_profile(self, updated_data):
        id = updated_data[0]
        name = updated_data[1]
        subject = updated_data[2]
        email = updated_data[3]
        gender = updated_data[4]
        contact = updated_data[5]
        dob = updated_data[6]
        experience = updated_data[7]


        cursor = self.connection.cursor()
        cursor.execute(
            "UPDATE faculties SET name=%s, subject=%s, email=%s, gender=%s, contact=%s, dob=%s, experience=%s WHERE id=%s",
            (name, subject, email, gender, contact, dob, experience, id))
        self.connection.commit()



if __name__ == "__main__":
    root = tk.Tk()
    welcome_page = facultyHomePage(root)
    root.mainloop()
