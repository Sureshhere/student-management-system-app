import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkcalendar
from datetime import datetime
from PIL import ImageTk, Image


class Attendance:
    def __init__(self, master):
        self.master = master
        self.master.title("Student Attendance")
        self.master.geometry('500x700')
        self.master.resizable(False, False)

        # Database Connection
        try:
            self.connection = mysql.connector.connect(host="localhost", user="root", password="sureshchoudhary",
                                                      database="stdmng")
        except mysql.connector.Error as error:
            messagebox.showerror("Database Error", f"Failed to connect to the database: {error}")
            self.master.destroy()


        self.title = ttk.Label(self.master,text="Take Student Attendance",padding=(150,10),font=('Arial',15),background='#000338',foreground="white",width=600)
        self.title.place(x=0,y=10)

        select_division = ttk.Label(self.master, text="Select section:",font=('Arial',12))
        select_division.place(x=30, y=80)

        self.divisions_combobox = ttk.Combobox(self.master, state="readonly", width=20,font=('Arial',12))

        self.divisions_combobox['values'] = ("Data Science", "AIML", "Cyber Security", "IT", "IoT")
        self.divisions_mapping = {"Data Science": "data_science",
                                  "AIML": "aiml",
                                  "Cyber Security": "cyber_security",
                                  "IT": "it",
                                  "IoT": "iot"
                                  }

        self.divisions_combobox.current(0)
        self.divisions_combobox.place(x=140, y=80)


        get_details_button = ttk.Button(self.master, text="Get Details", command=self.get_details)
        get_details_button.place(x=350, y=75)

        search_label = ttk.Label(self.master, text="Search roll no:",font=('Arial',12))
        search_label.place(x=30, y=120)

        self.search_entry = ttk.Entry(self.master, width=30)
        self.search_entry.place(x=140, y=120)

        search_button = ttk.Button(self.master, text="Search", command=self.search_attendance)
        search_button.place(x=350, y=120)

        self.lbl_date = ttk.Label(self.master,text="Select date:",font=('Arial',12))
        self.lbl_date.place(x=145,y=155)
        self.date_entry = tkcalendar.DateEntry(self.master, width=12, background='darkblue', foreground='white',
                                               borderwidth=2, date_pattern='dd/mm/yyyy')
        self.date_entry.place(x=240, y=155)

        update_button = ttk.Button(self.master, text="Update", command=self.update_attendance)
        update_button.place(x=130, y=190)

        # Clear Button
        clear_button = ttk.Button(self.master, text="Clear", command=self.clear_attendance)
        clear_button.place(x=350, y=190)

        # Attendance Records
        self.attendance_records = []
        self.checkboxes = []

    def get_details(self):
        displayed_division = self.divisions_combobox.get()
        table_name = self.divisions_mapping.get(displayed_division)

        if table_name:
            # Clear previous results
            for checkbox in self.checkboxes:
                checkbox[0].destroy()
                checkbox[1].destroy()
                checkbox[2].destroy()

            self.checkboxes = []

            query = f"SELECT roll_no, name FROM {table_name} WHERE section = '{displayed_division}';"
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.attendance_records = cursor.fetchall()

            start = 220
            for roll_no, name in self.attendance_records:
                records_label = ttk.Label(self.master, text=f"{roll_no}\t{name}",font=('Arial',10))
                records_label.place(x=50, y=start)

                var = tk.StringVar(value='Absent')
                present_radio = ttk.Radiobutton(self.master, text='Present', variable=var, value='Present')
                present_radio.place(x=300, y=start)
                absent_radio = ttk.Radiobutton(self.master, text='Absent', variable=var, value='Absent')
                absent_radio.place(x=380, y=start)

                self.checkboxes.append((records_label, present_radio, absent_radio, roll_no, name, var))

                start += 20
        else:
            messagebox.showerror("Error", "Invalid division selected!")

    def search_attendance(self):
        displayed_division = self.divisions_combobox.get()
        table_name = self.divisions_mapping.get(displayed_division)
        enrollment = self.search_entry.get()

        if table_name:
            # Clear previous results
            for checkbox in self.checkboxes:
                checkbox[0].destroy()
                checkbox[1].destroy()
                checkbox[2].destroy()

            self.checkboxes = []

            query = f"SELECT roll_no, name FROM {table_name} WHERE roll_no = '{enrollment}' " \
                    f"AND section = '{displayed_division}';"  # Modified column name from 'enrollment' to 'roll_no'
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.attendance_records = cursor.fetchall()

            if self.attendance_records:
                start = 220
                for roll_no, name in self.attendance_records:
                    records_label = ttk.Label(self.master, text=f"{roll_no} {name}")
                    records_label.place(x=110, y=start)

                    var = tk.StringVar(value='Absent')
                    present_radio = ttk.Radiobutton(self.master, text='Present', variable=var, value='Present')
                    present_radio.place(x=350, y=start)
                    absent_radio = ttk.Radiobutton(self.master, text='Absent', variable=var, value='Absent')
                    absent_radio.place(x=410, y=start)

                    self.checkboxes.append((records_label, present_radio, absent_radio, roll_no, name, var))

                    start += 20
            else:
                messagebox.showinfo("Not Found", "No records found for the entered enrollment!")
        else:
            messagebox.showerror("Error", "Invalid division selected!")

    def update_attendance(self):
        selected_date = self.date_entry.get()
        formatted_date = datetime.strptime(selected_date, '%d/%m/%Y').strftime('%Y-%m-%d')

        cursor = self.connection.cursor()
        displayed_division = self.divisions_combobox.get()
        table_name = self.divisions_mapping.get(displayed_division)

        if table_name:
            for _, _, _, enrollment, name, var in self.checkboxes:
                status = var.get()

                query = "SELECT * FROM attendance WHERE enrollment = %s AND date_day = %s AND division_name = %s"
                values = (enrollment, formatted_date, table_name)
                cursor.execute(query, values)
                result = cursor.fetchone()

                if result:
                    query = "UPDATE attendance SET status = %s WHERE enrollment = %s AND date_day = %s AND division_name = %s"
                    update_values = (status, enrollment, formatted_date, table_name)
                    cursor.execute(query, update_values)
                else:
                    query = "INSERT INTO attendance (enrollment, name, status, date_day, division_name) VALUES (%s, %s, %s, %s, %s)"
                    insert_values = (enrollment, name, status, formatted_date, table_name)
                    cursor.execute(query, insert_values)

            self.connection.commit()
            messagebox.showinfo("Success", "Attendance updated successfully!")
        else:
            messagebox.showerror("Error", "Invalid division selected!")

    def clear_attendance(self):
        for _, _, _, _, _, var in self.checkboxes:
            var.set('Absent')


if __name__ == "__main__":
    root = tk.Tk()
    app = Attendance(root)
    root.mainloop()
