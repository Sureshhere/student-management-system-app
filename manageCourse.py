from tkinter import *
from tkinter import ttk, messagebox
import pymysql
import os
import tkinter as tk
from _tkinter import *
from tkinter.ttk import Combobox


class Course():
     def __init__(self, root):
        self.root = root
        self.root.title("student management system")
        root.attributes('-fullscreen', True)



        title = Label(self.root,text="Student Management System" ,bd=9,relief=GROOVE, font=("times new roman",50,"bold"),bg="#f98129",fg="darkblue")
        title.pack(side=TOP,fill=X)
        #============== All Variables db========================================
        self.Course_id_var = StringVar()
        self.course_name_var = StringVar()
        self.faculty_var = StringVar()
        self.gender_var = StringVar()
        self.course_credits_var = StringVar()
        self.dob_var = StringVar()
        self.section_var = StringVar()
        self.password_var = StringVar()



        #==============Manageframe============================================
        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="blue")
        Manage_Frame.place(x=20,y=100,width=450,height=685)

        m_title = Label(Manage_Frame,text="Manage Course", bg="yellow",fg="black",font=("times new roman",30,"bold"))
        m_title.grid(row=0 ,columnspan=2,pady=(10,10))

        lbl_roll = Label(Manage_Frame,text="Course ID:", bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1 ,column=0,pady=10,padx=0,sticky="w")
        txt_Roll=Entry(Manage_Frame, textvariable=self.Course_id_var, font=("times new roman", 15, "bold"), bd=5, relief=RAISED)
        txt_Roll.grid(row=1 ,column=1,pady=10,padx=20,sticky="w")

        lbl_name = Label(Manage_Frame, text="Course Name:", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=0, sticky="w")
        txt_name = Entry(Manage_Frame, textvariable=self.course_name_var, font=("times new roman", 15, "bold"), bd=5, relief=RAISED)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_Email = Label(Manage_Frame, text="Faculty:",bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_Email.grid(row=3, column=0, pady=10, padx=0, sticky="w")
        txt_Email = Entry(Manage_Frame, textvariable=self.faculty_var, font=("times new roman", 15, "bold"), bd=5, relief=RAISED)
        txt_Email.grid(row=3, column=1, pady=10, padx=20, sticky="w")



        lbl_Contact = Label(Manage_Frame, text="Course Credits:",bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_Contact.grid(row=5, column=0, pady=10, padx=0, sticky="w")
        txt_Contact = Entry(Manage_Frame, textvariable=self.course_credits_var, font=("times new roman", 15, "bold"), bd=5, relief=RAISED)
        txt_Contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")




        #=========Button Frame==================
        btn_Frame = Frame(Manage_Frame, bd=3, relief=RIDGE, bg="gray")
        btn_Frame.place(x=0, y=625, width=442)


   # =========2nd Detials  Frame==================
        Detials_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="blue")
        Detials_Frame.place(x=500, y=100, width=980, height=685)

        # -------- MANAGE BUTTONS --------------
        Addbtn = Button(Detials_Frame, text="Add", width=10, font=('Arial', 15,"bold"),background="#f98129",foreground="white",activeforeground="white",activebackground="#f98120", relief=RAISED, borderwidth=10, command=self.add_students).place(x=100,y=600)
        updatebtn = Button(Detials_Frame, text="Update", width=10, font=('Arial', 15,"bold"),background="#f98129",foreground="white",activeforeground="white",activebackground="#f98120", relief=RAISED, borderwidth=10, command=self.update_data).place(x=300,y=600)
        deletebtn = Button(Detials_Frame, text="Delete", width=10, font=('Arial', 15,"bold"),background="#f98129",foreground="white",activeforeground="white",activebackground="#f98120", relief=RAISED, borderwidth=10, command=self.delete_data).place(x=500,y=600)
        Clearbtn = Button(Detials_Frame, text="Clear", width=10, font=('Arial', 15,"bold"),background="#f98129",foreground="white",activeforeground="white",activebackground="#f98120", relief=RAISED, borderwidth=10, command=self.clear).place(x=700,y=600)

        dashboardBtn = Button(Detials_Frame, text="Go to\nDashboard", width=15, pady=5,command=self.gotoDashboard, font=('Arial', 11,"bold"),background="green",foreground="white",activeforeground="white",activebackground="darkgreen", relief=RAISED, borderwidth=5,).grid(row=0,column=5,padx=(800,0),pady=(10))
#========== table frame ===========
        Table_Frame = Frame(Detials_Frame, bd=4, relief=RIDGE, bg="crimson")
        Table_Frame.place(x=10, y=95, width=940, height=500)

        scroll_x = Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_table = ttk.Treeview(Table_Frame,column=("course_id","course_name","faculty","course_credits"),
                                          xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        # ---- Column head styling ----
        style = ttk.Style()
        style.configure("Treeview.Heading", background="red", foreground="black")
        tree = ttk.Treeview(root, style="Treeview")

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("course_id",text="Course ID")
        self.Student_table.heading("course_name", text="Course Name")
        self.Student_table.heading("faculty", text="Faculty")
        self.Student_table.heading("course_credits", text="Course Credits")


        self.Student_table['show'] = 'headings'
        self.Student_table.column("course_id",width=100,anchor=S)
        self.Student_table.column("course_name", width=100,anchor=S)
        self.Student_table.column("faculty", width=100,anchor=S)
        self.Student_table.column("course_credits", width=100,anchor=S)


        self.Student_table.pack(fill=BOTH , expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()

     def add_students(self):
         if self.Course_id_var.get() == "" or self.course_name_var.get() == "":
             messagebox.showerror("Error", "All fields are required")
         else:
             con = pymysql.connect(host="localhost", user="root", password="sureshchoudhary", database="stdmng")
             cur = con.cursor()

             # Check if roll number already exists
             cur.execute("SELECT * FROM courses WHERE course_id = %s", self.Course_id_var.get())
             existing_row = cur.fetchone()
             if existing_row:
                 messagebox.showerror("Error", "Course id already exists")
             else:
                 cur.execute("INSERT INTO courses VALUES(%s,%s,%s,%s)", (
                     self.Course_id_var.get(),
                     self.course_name_var.get(),
                     self.faculty_var.get(),
                     self.course_credits_var.get()
                 ))

                 con.commit()
                 self.fetch_data()
                 self.clear()
                 con.close()
                 messagebox.showinfo("Success", "Record has been inserted")

     def fetch_data(self):
         con = pymysql.connect(host="localhost", user="root", password="sureshchoudhary", database="stdmng")
         cur = con.cursor()
         cur.execute("SELECT * FROM courses ")
         rows = cur.fetchall()
         if len(rows) != 0:
             self.Student_table.delete(*self.Student_table.get_children())
             for row in rows:
                 self.Student_table.insert('', END, values=row)

             con.commit()
         con.close()

     def clear(self):
         self.Course_id_var.set("")
         self.faculty_var.set("")
         self.course_name_var.set("")
         self.course_credits_var.set("")

     def get_cursor(self, ev):
         cursor_row = self.Student_table.focus()
         contents = self.Student_table.item(cursor_row)
         row = contents['values']
         if len(row) > 0:
             self.Course_id_var.set(row[0])
             self.course_name_var.set(row[1])

             self.faculty_var.set(row[2])

             self.course_credits_var.set(row[3])

     def update_data(self):
         con = pymysql.connect(host="localhost", user="root", password="sureshchoudhary", database="stdmng")
         cur = con.cursor()
         cur.execute(
             "UPDATE courses SET course_id=%s, course_name=%s, faculty=%s, course_credits=%s WHERE course_id=%s",
             (
                 self.Course_id_var.get(),
                 self.course_name_var.get(),
                 self.faculty_var.get(),
                 self.course_credits_var.get(),
                 self.Course_id_var.get()
             )
         )

         con.commit()
         self.fetch_data()
         self.clear()
         con.close()

     def delete_data(self):
         con = pymysql.connect(host="localhost", user="root", password="sureshchoudhary", database="stdmng")
         cur = con.cursor()
         cur.execute("delete from courses where course_id=%s", self.Course_id_var.get())
         con.commit()
         con.close()
         self.fetch_data()
         self.clear()



     def gotoDashboard(self):
         self.root.destroy()
         os.system("python adminHomepage.py")
class Course():
    pass
    root=Tk()
    ob=Course(root)
    root.mainloop()