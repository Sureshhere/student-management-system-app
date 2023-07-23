from tkinter import *
from tkinter import ttk, messagebox
import pymysql
import os
import tkinter as tk
from _tkinter import *
from tkinter.ttk import Combobox


class Student():
     def __init__(self, root):
        self.root = root
        self.root.title("student management system")
        root.attributes('-fullscreen', True)



        title = Label(self.root,text="Student Management System" ,bd=9,relief=GROOVE, font=("times new roman",50,"bold"),bg="#f98129",fg="darkblue")
        title.pack(side=TOP,fill=X)
        #============== All Variables db========================================
        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        self.section_var = StringVar()
        self.password_var = StringVar()

        self.search_by=StringVar()
        self.search_txt = StringVar()

        #==============Manageframe============================================
        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="blue")
        Manage_Frame.place(x=20,y=100,width=450,height=685)

        m_title = Label(Manage_Frame,text="Manage Student", bg="yellow",fg="black",font=("times new roman",30,"bold"))
        m_title.grid(row=0 ,columnspan=2,pady=(10,10))

        lbl_roll = Label(Manage_Frame,text="Roll No:", bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1 ,column=0,pady=10,padx=20,sticky="w")
        txt_Roll=Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("times new roman",15,"bold"),bd=5,relief=RAISED)
        txt_Roll.grid(row=1 ,column=1,pady=10,padx=20,sticky="w")

        lbl_name = Label(Manage_Frame, text="Name:", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        txt_name = Entry(Manage_Frame,textvariable=self.name_var, font=("times new roman", 15, "bold"), bd=5, relief=RAISED)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_Email = Label(Manage_Frame, text="Email:",bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_Email.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        txt_Email = Entry(Manage_Frame, textvariable=self.email_var,font=("times new roman", 15, "bold"), bd=5, relief=RAISED)
        txt_Email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_Gender = Label(Manage_Frame, text="Gender:", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_Gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        combo_gender = ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman", 20, "bold"),width=13 ,state='readonly')
        combo_gender['values'] = ("Male","Female","other")

        combo_gender.grid(row=4,column=1,padx=20,pady=10)

        lbl_Contact = Label(Manage_Frame, text="Contact:",bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_Contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        txt_Contact = Entry(Manage_Frame,textvariable=self.contact_var, font=("times new roman", 15, "bold"), bd=5, relief=RAISED)
        txt_Contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_Dob = Label(Manage_Frame, text="D.O.B:", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_Dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")
        txt_Dob = Entry(Manage_Frame,textvariable=self.dob_var, font=("times new roman", 15, "bold"), bd=5, relief=RAISED)
        txt_Dob.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_Address = Label(Manage_Frame, text="Address:", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_Address.grid(row=7, column=0, pady=10, padx=20, sticky="w")
        self.txt_Address = Text(Manage_Frame, width=30,height=3,font=("times new roman",10,"bold"))
        self.txt_Address.grid(row=7, column=1, pady=10, padx=20, sticky="w")
        # section
        lbl_Section = Label(Manage_Frame, text="Section:", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_Section.grid(row=8, column=0, pady=10, padx=20, sticky="w")
        txt_Section = Entry(Manage_Frame, textvariable=self.section_var, font=("times new roman", 15, "bold"), bd=5,
                            relief=RAISED)
        txt_Section.grid(row=8, column=1, pady=10, padx=20, sticky="w")

        # password
        lbl_Password = Label(Manage_Frame, text="Password:", bg="blue", fg="white",
                             font=("times new roman", 20, "bold"))
        lbl_Password.grid(row=9, column=0, pady=10, padx=20, sticky="w")
        txt_Password = Entry(Manage_Frame, textvariable=self.password_var, font=("times new roman", 15, "bold"), bd=5, relief=RAISED)
        txt_Password.grid(row=9, column=1, pady=10, padx=20, sticky="w")

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


        lbl_search = Label(Detials_Frame, text="Sort By", bg="blue", fg="white",font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=10, sticky="w")


        combo_search = ttk.Combobox(Detials_Frame,textvariable=self.search_by,width=10, font=("times new roman", 13, "bold"), state='readonly')
        combo_search['values'] = ("roll_no", "Section", "Gender","Name","Contact")
        combo_search.grid(row=0, column=1, padx=20, pady=10)

        txt_search= Entry(Detials_Frame,textvariable=self.search_txt,width=20, font=("consolas", 15), bd=5, relief=SUNKEN)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchbtn = Button(Detials_Frame, text="Search", width=10,pady=5,command=self.search_data, font=('Arial', 10,"bold"),background="#f98129",foreground="white",activeforeground="white",activebackground="#f98120", relief=RAISED, borderwidth=5).grid(row=0, column=3, padx=10, pady=10)
        showallbtn = Button(Detials_Frame, text="Show All", width=10, pady=5,command=self.fetch_data, font=('Arial', 10,"bold"),background="#f98129",foreground="white",activeforeground="white",activebackground="#f98120", relief=RAISED, borderwidth=5,).grid(row=0, column=4, padx=10, pady=10)

        dashboardBtn = Button(Detials_Frame, text="Go to\nDashboard", width=15, pady=5,command=self.gotoDashboard, font=('Arial', 11,"bold"),background="green",foreground="white",activeforeground="white",activebackground="darkgreen", relief=RAISED, borderwidth=5,).grid(row=0,column=5,padx=(40,0),pady=(10))
#========== table frame ===========
        Table_Frame = Frame(Detials_Frame, bd=4, relief=RIDGE, bg="crimson")
        Table_Frame.place(x=10, y=95, width=940, height=500)

        scroll_x = Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_table = ttk.Treeview(Table_Frame,column=("roll","name","section","password","email","gender","contact","dob","Address"),
                                          xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        # ---- Column head styling ----
        style = ttk.Style()
        style.configure("Treeview.Heading", background="red", foreground="black")
        tree = ttk.Treeview(root, style="Treeview")

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("roll",text="Roll NO.")
        self.Student_table.heading("name", text="Name")
        self.Student_table.heading("section", text="Section")
        self.Student_table.heading("password", text="Password")
        self.Student_table.heading("email", text="Email")
        self.Student_table.heading("gender", text="Gender")
        self.Student_table.heading("contact", text="Contact")
        self.Student_table.heading("dob", text="D.O.B")
        self.Student_table.heading("Address", text="Address")

        self.Student_table['show'] = 'headings'
        self.Student_table.column("roll",width=100)
        self.Student_table.column("name", width=100)
        self.Student_table.column("section", width=100)
        self.Student_table.column("password", width=100)
        self.Student_table.column("email", width=100)
        self.Student_table.column("gender", width=100)
        self.Student_table.column("contact", width=100)
        self.Student_table.column("dob", width=100)
        self.Student_table.column("Address", width=150)

        self.Student_table.pack(fill=BOTH , expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()

     def add_students(self):
         if self.Roll_No_var.get() == "" or self.name_var.get() == "":
             messagebox.showerror("Error", "All fields are required")
         else:
             con = pymysql.connect(host="localhost", user="root", password="sureshchoudhary", database="stdmng")
             cur = con.cursor()

             # Check if roll number already exists
             cur.execute("SELECT * FROM students WHERE Roll_No = %s", self.Roll_No_var.get())
             existing_row = cur.fetchone()
             if existing_row:
                 messagebox.showerror("Error", "Roll number already exists")
             else:
                 cur.execute("INSERT INTO students VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                     self.Roll_No_var.get(),
                     self.name_var.get(),
                     self.section_var.get(),
                     self.password_var.get(),
                     self.email_var.get(),
                     self.gender_var.get(),
                     self.contact_var.get(),
                     self.dob_var.get(),
                     self.txt_Address.get('1.0', END)
                 ))

                 con.commit()
                 self.fetch_data()
                 self.clear()
                 con.close()
                 messagebox.showinfo("Success", "Record has been inserted")

     def fetch_data(self):
         con = pymysql.connect(host="localhost", user="root", password="sureshchoudhary", database="stdmng")
         cur = con.cursor()
         cur.execute("SELECT * FROM students ")
         rows = cur.fetchall()
         if len(rows) != 0:
             self.Student_table.delete(*self.Student_table.get_children())
             for row in rows:
                 self.Student_table.insert('', END, values=row)

             con.commit()
         con.close()

     def clear(self):
         self.Roll_No_var.set("")
         self.name_var.set("")
         self.section_var.set("")
         self.password_var.set("")
         self.email_var.set("")
         self.gender_var.set("")
         self.contact_var.set("")
         self.dob_var.set("")
         self.txt_Address.delete("1.0",END)

     def get_cursor(self, ev):
         cursor_row = self.Student_table.focus()
         contents = self.Student_table.item(cursor_row)
         row = contents['values']
         if len(row) > 0:
             self.Roll_No_var.set(row[0])
             self.name_var.set(row[1])
             self.section_var.set(row[2])
             self.password_var.set(row[3])
             self.email_var.set(row[4])
             self.gender_var.set(row[5])
             self.contact_var.set(row[6])
             self.dob_var.set(row[7])
             self.txt_Address.delete("1.0", tk.END)
             self.txt_Address.insert(tk.END, row[8])

     def update_data(self):
         con = pymysql.connect(host="localhost", user="root", password="sureshchoudhary", database="stdmng")
         cur = con.cursor()
         cur.execute(
             "UPDATE students SET name=%s, section=%s, password=%s, email=%s, gender=%s, contact=%s, dob=%s, address=%s WHERE roll_no=%s",
             (
                 self.name_var.get(),
                 self.section_var.get(),
                 self.password_var.get(),
                 self.email_var.get(),
                 self.gender_var.get(),
                 self.contact_var.get(),
                 self.dob_var.get(),
                 self.txt_Address.get('1.0', END),
                 self.Roll_No_var.get()
             )
         )

         con.commit()
         self.fetch_data()
         self.clear()
         con.close()

     def delete_data(self):
         con = pymysql.connect(host="localhost", user="root", password="sureshchoudhary", database="stdmng")
         cur = con.cursor()
         cur.execute("delete from students where roll_no=%s",self.Roll_No_var.get())
         con.commit()
         con.close()
         self.fetch_data()
         self.clear()

     def search_data(self):
         con = pymysql.connect(host="localhost", user="root", password="sureshchoudhary", database="stdmng")
         cur = con.cursor()
         search_term = self.search_txt.get()
         search_column = str(self.search_by.get())

         if search_column == "gender":
             cur.execute("SELECT * FROM students WHERE gender = %s", (search_term,))
         else:
             cur.execute("SELECT * FROM students WHERE " + search_column + " = %s", (search_term,))
         rows = cur.fetchall()

         if len(rows) != 0:
             self.Student_table.delete(*self.Student_table.get_children())
             for row in rows:
                 self.Student_table.insert('', END, values=row)
             con.commit()
         con.close()

     def gotoDashboard(self):
         self.root.destroy()
         os.system("python adminHomepage.py")
class Student():
    pass
    root=Tk()
    ob=Student(root)
    root.mainloop()