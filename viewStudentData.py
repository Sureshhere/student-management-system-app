import tkinter as tk
from tkinter import ttk
from ttkbootstrap import *
import mysql.connector

# Create a MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sureshchoudhary",
    database="stdmng"
)

cursor = db.cursor()

def display_students():
    for widget in window.winfo_children():
        widget.destroy()

    treeview = ttk.Treeview(window,bootstyle='dark')
    treeview["columns"] = ("name", "section", "email", "gender", "contact", "dob", "address")
    treeview.heading("#0", text="Roll No")
    treeview.heading("name", text="Name")
    treeview.heading("section", text="Section")
    treeview.heading("email", text="Email")
    treeview.heading("gender", text="Gender")
    treeview.heading("contact", text="Contact")
    treeview.heading("dob", text="Date of Birth")
    treeview.heading("address", text="Address")
    treeview.pack()

    # Fetch student details from the database
    query = "SELECT * FROM students"
    cursor.execute(query)
    students = cursor.fetchall()

    for student in students:
        roll_no = student[0]
        name = student[1]
        section = student[2]
        email = student[4]
        gender = student[5]
        contact = student[6]
        dob = student[7]
        address = student[8]
        treeview.insert("", "end", text=roll_no, values=(name, section, email, gender, contact, dob, address))

window = tk.Tk()
window.title("Faculty Window")
window.attributes('-fullscreen', True)

btn_display = tk.Button(window, text="Display Student Details", command=display_students)
btn_display.pack()

window.mainloop()

db.close()
