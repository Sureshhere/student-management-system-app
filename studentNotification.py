import tkinter as tk
import mysql.connector
from tkinter import messagebox

class StudentApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x600")
        self.root.title("Student Notification App")
        self.db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sureshchoudhary",
            database="stdmng"
        )
        self.create_table()
        self.show_notifications()

    def create_table(self):
        cursor = self.db_connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS notifications (title VARCHAR(255), message TEXT, recipients TEXT, date DATE)")
        self.db_connection.commit()

    def show_notifications(self):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT title, message, recipients, date FROM notifications WHERE recipients IN ('Students', 'Faculty, Students') ORDER BY date DESC")
        notifications = cursor.fetchall()

        notifications_frame = tk.Frame(self.root, bg="#EDEDED")
        notifications_frame.pack(padx=20, pady=20)

        tk.Label(notifications_frame, text="Notifications", font=("Arial", 20, "bold"), bg="#EDEDED").pack(pady=10)

        canvas = tk.Canvas(notifications_frame, bg="#EDEDED", width=500,height=600)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(notifications_frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))

        notifications_inner_frame = tk.Frame(canvas, bg="#EDEDED")
        notifications_inner_frame.pack(fill="both", expand=True)

        canvas.create_window((0, 0), window=notifications_inner_frame, anchor="nw")

        if notifications:
            for i, notification in enumerate(notifications, start=1):
                tk.Label(notifications_inner_frame, text=f"Title {notification[0]}", font=("Arial", 12, "bold underline"), bg="#003487", fg="#ffffff",width=44,padx=4).pack()
                tk.Label(notifications_inner_frame, text=f"Date: {notification[3]}", font=("Arial", 12, "italic"), bg="#d4d4d4", fg='brown',width=48,padx=8).pack()
                tk.Label(notifications_inner_frame, text=f"{notification[1]}", font=("Arial", 12), bg="#d4d4d4", fg='black', wraplength=450, justify="left",width=48,padx=8).pack()
                tk.Label(notifications_inner_frame, text="---------------------------------------", bg="#EDEDED").pack()
        else:
            tk.Label(notifications_inner_frame, text="No messages available.", font=("Arial", 12), bg="#EDEDED").pack()

        canvas.configure(scrollregion=canvas.bbox("all"))

    def run(self):
        self.root.mainloop()

# Create an instance of the StudentApp class and run the student application
app = StudentApp()
app.run()
