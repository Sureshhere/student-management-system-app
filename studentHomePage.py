import tkinter as tk
from tkinter import *
from tkinter import messagebox,ttk,Tk,Label
import os
from PIL import ImageTk, Image
import mysql.connector
import webview

class studentHomePage:
    def __init__(self, root,roll_no="2111cs030133"):
        self.root = root
        self.roll_no = roll_no
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
        self.lbl_rollno = tk.Label(self.root,text="Account: "+self.roll_no,font=("Arial", 18),background='#000338',foreground="white")
        self.lbl_rollno.place(x=10,y=10)

        self.label = tk.Label(self.root, text="STUDENT DASHBOARD",
                              font=("Arial", 38, 'underline'))
        self.label.pack(pady=10)

        self.label = tk.Label(self.root, text="Malla Reddy University", font=("Arial", 28))
        self.label.pack(pady=10)

        # ------ student profile--------

        self.image = tk.PhotoImage(file="imgs/profile2.png",height=100,width=100)
        self.button1 = tk.Button(self.root, text="Profile",width=250, compound=tk.TOP, font=('Arial', 20),
                                 image=self.image, command=self.view_profile,relief=RAISED,borderwidth=7,background='orange')
        self.button1.place(x=100, y=200)

        # ---- faculty button----

        self.image2 = tk.PhotoImage(file="imgs/bar-chart-100.png")
        self.button2 = tk.Button(self.root, text="Exam Marks Report",width=230, compound=tk.TOP, font=('Arial', 20), image=self.image2,
                                 command=self.getMarksReport, relief=RAISED,padx=20,borderwidth=7,background='orange')
        self.button2.place(x=450, y=200)

        # ---- student attendance button----

        self.image3 = tk.PhotoImage(file="imgs/attendanceImg.png")
        self.button3 = tk.Button(self.root, text="Student Attendance", compound=tk.TOP, font=('Arial', 20),
                                 image=self.image3,
                                 command=self.show_attendance,
                                 relief=RAISED,
                                 borderwidth=7,
                                 background='orange')
        self.button3.place(x=805, y=200)




        # ---- apply leave button----

        self.image5 = tk.PhotoImage(file="imgs/leave.png", height=96)
        self.button5 = tk.Button(self.root, text="Apply for leave",width=250, compound=tk.TOP, font=('Arial', 20),
                                 image=self.image5,
                                 command=self.applyLeave,
                                 relief=RAISED,
                                 borderwidth=7,
                                 background='orange')
        self.button5.place(x=100, y=450)

        # ---- send notification/mails button----

        self.image6 = tk.PhotoImage(file="imgs/chat.png", height=96)
        self.button6 = tk.Button(self.root, text="Notification",width=260, compound=tk.TOP, font=('Arial', 20),
                                 image=self.image6,
                                 command=self.studentNotification,
                                 relief=RAISED,
                                 borderwidth=7,
                                 background='orange')
        self.button6.place(x=450, y=450)



        # ---- view profile button ----

        # self.image7 = tk.PhotoImage(file="imgs/profile.png", height=96)
        # self.button7 = tk.Button(self.root, text="View Profile", width=230, compound=tk.TOP, font=('Arial', 20),
        #                          image=self.image7,
        #                          command=self.view_profile,
        #                          relief=RAISED,
        #                          padx=20,
        #                          borderwidth=7,
        #                          background='orange')
        # self.button7.place(x=805, y=450)

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

    def getMarksReport(self):
        os.system("python indivStdMarksAnalysis.py")
    def applyLeave(self):
        webview.create_window('Apply for a leave', 'website/studentapplyleave.html',height=900)
        webview.start()

    def show_attendance(self):
        cursor = self.connection.cursor()

        query = """
        SELECT date_day, status
        FROM attendance
        WHERE enrollment = %s;
        """

        cursor.execute(query, (self.roll_no,))
        attendance_data = cursor.fetchall()
        cursor.close()

        attendance_window = tk.Toplevel(self.root)
        attendance_window.title("Attendance")
        attendance_window.geometry("500x400")

        total_classes = len(attendance_data)
        total_absent = sum(1 for data in attendance_data if data[1] == 'Absent')

        label_name =  tk.Label(attendance_window, text="" + self.roll_no, font=("Arial", 12,'underline'))
        label_name.pack(padx=0,pady=(10,5))

        label_classes = tk.Label(attendance_window, text="Total Classes: " + str(total_classes), font=("Arial", 12))
        label_classes.pack(padx=0,pady=(10,5))

        label_absent = tk.Label(attendance_window, text="Days Absent: " + str(total_absent), font=("Arial", 12))
        label_absent.pack(padx=0,pady=(2,10))

        tree_frame = tk.Frame(attendance_window)
        tree_frame.pack()

        treeview = ttk.Treeview(tree_frame)
        treeview["columns"] = ("Date", "Status")

        treeview.column("#0", width=0, stretch=tk.NO)
        treeview.column("Date", anchor=tk.CENTER, width=150)
        treeview.column("Status", anchor=tk.CENTER, width=150)

        treeview.heading("#0", text="", anchor=tk.CENTER)
        treeview.heading("Date", text="Date", anchor=tk.CENTER)
        treeview.heading("Status", text="Status", anchor=tk.CENTER)

        scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=treeview.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        treeview.configure(yscrollcommand=scrollbar.set)
        treeview.pack(side=tk.LEFT, fill=tk.BOTH)

        for data in attendance_data:
            treeview.insert("", tk.END, text="", values=(data[0], data[1]))

        attendance_window.mainloop()

    def get_student_profile(self, roll_no):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM students WHERE roll_no=%s", (roll_no,))
            student_data = cursor.fetchone()
            return student_data
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Error fetching student profile: {error}")
            return None

    def view_profile(self):
        roll_no = self.roll_no
        student_data = self.get_student_profile(roll_no)
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
            tree.insert("", tk.END, text="", values=("Roll No", student_data[0]))
            tree.insert("", tk.END, text="", values=("Name", student_data[1]))
            tree.insert("", tk.END, text="", values=("Section", student_data[2]))
            # tree.insert("", tk.END, text="", values=("Password", '********'))  # Remove this line
            tree.insert("", tk.END, text="", values=("Email", student_data[4]))
            tree.insert("", tk.END, text="", values=("Gender", student_data[5]))
            tree.insert("", tk.END, text="", values=("Contact", student_data[6]))
            tree.insert("", tk.END, text="", values=("DOB", student_data[7]))
            tree.insert("", tk.END, text="", values=("Address", student_data[8]))

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
        roll_no_label = Label(edit_window, text="Roll No:", font=('Arial', 13))
        roll_no_entry = Entry(edit_window, font=('arial', 13))
        roll_no_label.pack()
        roll_no_entry.pack()

        name_label = Label(edit_window, text="Name:", font=('Arial', 13))
        name_entry = Entry(edit_window, font=('arial', 13))
        name_label.pack()
        name_entry.pack()

        section_label = Label(edit_window, text="Section:", font=('Arial', 13))
        section_entry = Entry(edit_window, font=('arial', 13))
        section_label.pack()
        section_entry.pack()

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

        address_label = Label(edit_window, text="Address:", font=('Arial', 13))
        address_entry = Entry(edit_window, font=('arial', 13),width=25)
        address_label.pack()
        address_entry.pack()

        # Set the initial values of the entry fields with the student data
        roll_no_entry.insert(0, student_data[0])
        name_entry.insert(0, student_data[1])
        section_entry.insert(0, student_data[2])
        email_entry.insert(0, student_data[4])
        gender_entry.insert(0, student_data[5])
        contact_entry.insert(0, student_data[6])
        dob_entry.insert(0, student_data[7])
        address_entry.insert(0, student_data[8])

        # Update the student profile when the Save button is clicked
        def save_profile():
            new_roll_no = roll_no_entry.get()
            new_name = name_entry.get()
            new_section = section_entry.get()
            new_email = email_entry.get()
            new_gender = gender_entry.get()
            new_contact = contact_entry.get()
            new_dob = dob_entry.get()
            new_address = address_entry.get()

            # Update the student profile in the database
            # Replace this code with your actual database update logic
            updated_data = (
            new_roll_no, new_name, new_section, new_email, new_gender, new_contact, new_dob, new_address)
            self.update_student_profile(updated_data)

            # Display a success message
            messagebox.showinfo("Success", "Profile updated successfully")

            # Destroy the edit window
            edit_window.destroy()
            profile_window.destroy()

        save_button = Button(edit_window, text="Save", command=save_profile)
        save_button.pack(pady=10)

    def update_student_profile(self, updated_data):
        roll_no = updated_data[0]
        name = updated_data[1]
        section = updated_data[2]
        email = updated_data[3]
        gender = updated_data[4]
        contact = updated_data[5]
        dob = updated_data[6]
        address = updated_data[7]

        cursor = self.connection.cursor()
        cursor.execute(
            "UPDATE students SET name=%s, section=%s, email=%s, gender=%s, contact=%s, dob=%s, address=%s WHERE roll_no=%s",
            (name, section, email, gender, contact, dob, address, roll_no))


        self.connection.commit()

    def studentNotification(self):
        os.system("python studentNotification.py")


if __name__ == "__main__":
    def get_roll_number():
        return rollNo
    root = tk.Tk()
    welcome_page = studentHomePage(root)
    root.mainloop()
