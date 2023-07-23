import tkinter as tk
from tkinter import ttk, messagebox,END
import pandas as pd
import matplotlib.pyplot as plt
from PIL import ImageTk, Image

class StdMarksAnalysis:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Student marks analysis")
        # Background
        image = Image.open("imgs/wallpaper2.jpg")
        image = image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.LANCZOS)
        self.background_image = ImageTk.PhotoImage(image)
        style = ttk.Style()

        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        window_height = 600
        window_width = 800
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))
        self.root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))


        roll_number_label = ttk.Label(self.root, text="Roll Number:", font=('Arial', 18))
        roll_number_label.place(x=210, y=50)


        self.roll_number_entry = ttk.Entry(self.root, width=20, font=('Arial', 18))
        self.roll_number_entry.place(x=390, y=50)
        self.roll_number_entry.insert(END,'2111cs030133')


        # Analysis Buttons
        self.image1 = tk.PhotoImage(file="imgs/pie-chart-96.png", height=100, width=100)
        self.button1 = tk.Button(self.root, text="Scatter Plot", width=200, compound=tk.TOP, font=('Arial', 18),
                                 image=self.image1, command=self.plot_scatter, relief=tk.RAISED, borderwidth=7,
                                 background='orange')
        self.button1.place(x=100, y=200)

        self.image2 = tk.PhotoImage(file="imgs/bar-chart-100.png", height=100, width=100)
        self.button2 = tk.Button(self.root, text="Bar chart", width=200, compound=tk.TOP, font=('Arial', 18),
                                 image=self.image2, command=self.plot_bar, relief=tk.RAISED, borderwidth=7,
                                 background='orange')
        self.button2.place(x=450, y=200)



    def plot_scatter(self):
        roll_number = self.roll_number_entry.get()
        if roll_number:
            try:
                df = pd.read_csv("C:\\Users\\sures\\PycharmProjects\\AppDev\\sql\\student_data.csv")
                student_data = df[df['Roll Number'] == roll_number]
                if not student_data.empty:
                    marks_columns = ['Maths Marks', 'Java Marks', 'DAA Marks',"DAP Marks"]
                    for col in marks_columns:
                        plt.scatter(student_data.index, student_data[col], label=col)

                    plt.xlabel('Student Index')
                    plt.ylabel('Marks')
                    plt.title('Student Marks Scatter Plot ({})'.format(roll_number))
                    plt.legend()
                    plt.show()
                else:
                    messagebox.showwarning("Data Analysis", "No record found for the given roll number.")
            except FileNotFoundError:
                messagebox.showerror("Data Analysis", "Dataset file not found.")
        else:
            messagebox.showwarning("Data Analysis", "Please enter a roll number.")



    def plot_bar(self):
        columns = ['Maths Marks', 'Java Marks', 'DAA Marks',"DAP Marks"]
        roll_number = self.roll_number_entry.get()
        if roll_number:
            try:
                df = pd.read_csv("C:\\Users\\sures\\PycharmProjects\\AppDev\\sql\\student_data.csv")
                student_data = df[df['Roll Number'] == roll_number]
                if not student_data.empty:
                    for col in columns:
                        plt.bar(col, student_data[col])

                    plt.xlabel('Subject')
                    plt.ylabel('Marks')
                    plt.title('Bar Graph for Student ({})'.format(roll_number))
                    plt.show()
                else:
                    messagebox.showwarning("Data Analysis", "No record found for the given roll number.")
            except FileNotFoundError:
                messagebox.showerror("Data Analysis", "Dataset file not found.")
        else:
            messagebox.showwarning("Data Analysis", "Please enter a roll number.")

    def run(self):
        self.root.mainloop()



app = StdMarksAnalysis()
app.run()
