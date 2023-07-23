import tkinter as tk
import mysql.connector
from tkinter import Label, Text, Button, Checkbutton, IntVar, messagebox, RAISED,SUNKEN
from datetime import datetime
from tkcalendar import DateEntry

class MyApp:
    def __init__(self):
        self.notificationRoot = tk.Tk()
        self.notificationRoot.geometry("1000x700")
        self.notificationRoot.configure(bg="#EDEDED")
        self.db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sureshchoudhary",
            database="stdmng"
        )
        self.create_table()
        self.notification_frame = None

    def create_table(self):
        cursor = self.db_connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS notifications (title VARCHAR(255), message TEXT, recipients TEXT, date DATETIME)")
        self.db_connection.commit()

    def open_notification_window(self):
        self.clear_content()
        self.notification_frame = tk.Frame(self.notificationRoot, bg="#EDEDED", highlightthickness=2,
                                           highlightbackground="black")
        self.notification_frame.grid(row=0, column=1, sticky="nsew")

        tk.Label(self.notification_frame, text="Notification Title:", font=("Arial", 12, "bold"), bg="#EDEDED").pack()
        self.title_text = tk.Entry(self.notification_frame, font=("Arial", 12))
        self.title_text.pack()
        self.title_text.insert(0, "Enter notification title")

        tk.Label(self.notification_frame, text="Message:", font=("Arial", 12, "bold"), bg="#EDEDED").pack()
        self.message_text = Text(self.notification_frame, font=("Arial", 12), wrap="word", height=10, width=40,
                                 borderwidth=4, relief=SUNKEN)
        self.message_text.pack(padx=15)

        tk.Label(self.notification_frame, text="Recipients:", font=("Arial", 12, "bold"), bg="#EDEDED").pack()
        self.faculty_var = IntVar()
        self.students_var = IntVar()
        tk.Checkbutton(self.notification_frame, text="Students", variable=self.students_var, font=("Arial", 12),
                       bg="#EDEDED").pack()

        tk.Label(self.notification_frame, text="Date:", font=("Arial", 12, "bold"), bg="#EDEDED").pack()
        self.date_text = DateEntry(self.notification_frame, font=("Arial", 12), date_pattern="yyyy-mm-dd")
        self.date_text.pack()

        tk.Button(self.notification_frame, text="Send", command=self.send_notification, font=("Arial", 12, "bold"),
                  bg="#FF8000", fg="white", relief=RAISED).pack()

    def send_notification(self):
        message = self.message_text.get("1.0", "end-1c")
        title = self.title_text.get()

        recipients = []
        if self.faculty_var.get():
            recipients.append("Faculty")
        if self.students_var.get():
            recipients.append("Students")

        if recipients:
            recipients_str = ", ".join(recipients)
            self.save_notification(title, message, recipients_str)
            messagebox.showinfo("Notification Sent", f"Notification sent to: {recipients_str}")
        else:
            messagebox.showwarning("No Recipients", "Please select at least one recipient.")

        self.clear_content()

    def save_notification(self, title, message, recipients):
        cursor = self.db_connection.cursor()
        now = datetime.now()
        cursor.execute("INSERT INTO notifications (title, message, recipients, date) VALUES (%s, %s, %s, %s)",
                       (title, message, recipients, now))
        self.db_connection.commit()

    def show_notifications(self):
        self.clear_content()
        self.notification_frame = tk.Frame(self.notificationRoot, bg="#EDEDED", highlightthickness=2,
                                           highlightbackground="black")
        self.notification_frame.grid(row=0, column=1, sticky="nsew")



        canvas = tk.Canvas(self.notification_frame, bg="#EDEDED", height=600, width=350)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(self.notification_frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))


        notifications_frame = tk.Frame(canvas, bg="#EDEDED")
        canvas.create_window((0, 0), window=notifications_frame, anchor="nw")

        cursor = self.db_connection.cursor()
        cursor.execute("SELECT title, message, recipients, date FROM notifications WHERE recipients IN ('Faculty', 'Faculty, Students') ORDER BY date DESC")

        notifications = cursor.fetchall()

        for i, notification in enumerate(notifications, start=1):
            tk.Label(notifications_frame, text=f"Title: {notification[0]}", font=("Arial", 12, "bold"), bg="#003487",
                     fg="#ffffff", width=35, padx=5).pack()
            tk.Label(notifications_frame, text=f"Date: {notification[3]}", font=("Arial", 12, "italic"),
                     bg="#d4d4d4", fg='brown', width=40).pack()

            tk.Label(notifications_frame, text=f"Recipients: {notification[1]}", font=("Arial", 12, "italic"),
                     bg="#d4d4d4", fg='black', width=40,wraplength=300).pack()

            tk.Label(notifications_frame, text="---------------------------------------", bg="#EDEDED").pack()

        canvas.configure(scrollregion=canvas.bbox("all"))

    def clear_content(self):
        if self.notification_frame is not None:
            self.notification_frame.destroy()
            self.notification_frame = None

    def run(self):
        self.notificationRoot.title("My App")

        left_frame = tk.Frame(self.notificationRoot, bg="#EDEDED")
        left_frame.grid(row=0, column=0, sticky="nsew")

        tk.Button(left_frame, text="Send Message/Notice", font=('Arial', 20, "bold"),
                  command=self.open_notification_window,
                  relief=RAISED,
                  borderwidth=7,
                  background='#FF8000', fg="white").pack(padx=(0,80),pady=30)

        tk.Button(left_frame, text="Show recent messages", font=('Arial', 20, "bold"),
                  command=self.show_notifications,
                  relief=RAISED,
                  borderwidth=7,
                  background='#FF8000', fg="white").pack(padx=(20,80),pady=30)

        self.notificationRoot.mainloop()

app = MyApp()
app.run()
