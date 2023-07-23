import tkinter as tk
from tkinter import filedialog
import pandas as pd
from tkinter import ttk,messagebox
from tkinter import *
from PIL import ImageTk, Image
import matplotlib.pyplot as plt

class DataAnalysisApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Student Marks Analysis App")

        # Background
        image = Image.open("imgs/wallpaper2.jpg")
        image = image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.LANCZOS)
        self.background_image = ImageTk.PhotoImage(image)
        style = ttk.Style()

        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        window_height = 700
        window_width = 1200
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))
        self.root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))

        # File Upload Section
        fileVar = Button(self.root, text="Open File", command=self.browse_file,
                         font=('Arial', 15),
                         foreground='white',
                         background='#ff4f00',
                         activebackground="#f98129",
                         activeforeground="white")
        fileVar.place(x=300, y=50)

        self.file_path = tk.StringVar()

        fileDir = ttk.Entry(self.root, textvariable=self.file_path, width=30, font=('Arial', 18))
        fileDir.place(x=420, y=50)

        style.configure('TFrame', background='#000338')
        section_frame = ttk.Frame(self.root)
        section_frame.place(x=450,y=110)

        section_label = ttk.Label(self.root, text="Select Section:", font=('Arial', 18))
        section_label.place(x=260, y=110)

        radio_frame = ttk.Frame(section_frame)
        radio_frame.pack()

        self.selected_section = tk.StringVar()


        style.configure('TRadiobutton', font=('Arial', 15),background='#000338',foreground='white')
        ttk.Radiobutton(radio_frame, text="Data Science", value="data science", variable=self.selected_section).pack(side="left",padx=(5,5))
        ttk.Radiobutton(radio_frame, text="IT", value="it", variable=self.selected_section).pack(side="left",padx=(5,5))
        ttk.Radiobutton(radio_frame, text="Cyber Security", value="cyber security", variable=self.selected_section).pack(side="left",padx=(5,5))
        ttk.Radiobutton(radio_frame, text="AIML", value="aiml", variable=self.selected_section).pack(side="left",padx=(5,5))
        ttk.Radiobutton(radio_frame, text="IoT", value="iot", variable=self.selected_section).pack(side="left",padx=(5,5))
        ttk.Radiobutton(radio_frame, text="All sections", value="all", variable=self.selected_section).pack(side="left",padx=(5,5))



        #  ----- analysis buttons---------
        self.image = tk.PhotoImage(file="imgs/pie-chart-96.png", height=100, width=100)
        self.button1 = tk.Button(self.root, text="Pass - Fail Report", width=200, compound=tk.TOP, font=('Arial', 18),
                                 image=self.image, command=self.analyze_data_piechart, relief=RAISED, borderwidth=7,
                                 background='orange')
        self.button1.place(x=100, y=200)

        self.image2 = tk.PhotoImage(file="imgs/scatter-plot-96.png", height=100, width=100)
        self.button2 = tk.Button(self.root, text="Scatter plot", width=200, compound=tk.TOP, font=('Arial', 18),
                                 image=self.image2, command=self.analyze_data_scatter, relief=RAISED, borderwidth=7,
                                 background='orange')
        self.button2.place(x=450, y=200)

        self.image3 = tk.PhotoImage(file="imgs/box-plot-64.png", height=100, width=100)
        self.button3 = tk.Button(self.root, text="Box Plot", width=200, compound=tk.TOP, font=('Arial', 18),
                                 image=self.image3, command=self.analyze_data_boxplot, relief=RAISED, borderwidth=7,
                                 background='orange')
        self.button3.place(x=800, y=200)

    def browse_file(self):
        file_types = [("CSV Files", "*.csv"), ("Excel Files", "*.xlsx")]
        file_path = filedialog.askopenfilename(filetypes=file_types)
        self.file_path.set(file_path)


    # ------------ pie chart-----------------
    def analyze_data_piechart(self):
        file_path = self.file_path.get()
        section = self.selected_section.get()

        if file_path:
            self.get_pie_chart(file_path, section)
        else:
            messagebox.showinfo("Error", "No file selected.")

    def get_pie_chart(self, file_path, section):
        try:
            df = pd.read_csv(file_path)
            if section != 'all':
                df = df[df['Section'] == section]

            pass_count = df['Pass/Fail'].value_counts().get('Pass', 0)
            fail_count = df['Pass/Fail'].value_counts().get('Fail', 0)

            if pass_count == 0 or fail_count == 0:
                print("No records found for the selected section.")
            else:
                labels = ['Pass', 'Fail']
                counts = [pass_count, fail_count]

                fig, ax = plt.subplots()
                ax.pie(counts, labels=labels, autopct='%1.1f%%')
                ax.set_title(f"Pass/Fail Analysis for {section} students" )
                plt.show()
        except FileNotFoundError:
            print("File not found.")

    # ------------- scatter plot--------------
    def analyze_data_scatter(self):
        file_path = self.file_path.get()
        section = self.selected_section.get()

        if file_path:
            self.get_scatter_plot(file_path, section)
        else:
            messagebox.showinfo("Error", "No file selected.")

    def get_scatter_plot(self, file_path, section):
        try:
            df = pd.read_csv(file_path)
            if section != 'all':
                df = df[df['Section'] == section]

            marks_columns = ['Maths Marks', 'Java Marks', 'DAA Marks','DAP Marks']

            fig, ax = plt.subplots()
            for col in marks_columns:
                plt.scatter(df.index, df[col], label=col)

            ax.set_xlabel('Student Index')
            ax.set_ylabel('Marks')
            ax.set_title(f'Student Marks Scatter Plot - {section} Section')
            ax.legend()
            plt.show()
        except FileNotFoundError:
            print("File not found.")

    # -------------- box plot---------------

    def analyze_data_boxplot(self):
        file_path = self.file_path.get()
        section = self.selected_section.get()

        if file_path:
            self.get_boxplot(file_path, section)
        else:
            messagebox.showinfo("Error", "No file selected.")

    def get_boxplot(self, file_path, section):
        try:
            df = pd.read_csv(file_path)
            if section != 'all':
                df = df[df['Section'] == section]

            marks_columns = ['Maths Marks', 'Java Marks', 'DAA Marks','DAP Marks']

            # Create a new figure and axes for the box plot
            fig, ax = plt.subplots()

            df[marks_columns].plot(kind='box', showfliers=False, ax=ax)

            ax.set_xlabel('Subjects')
            ax.set_ylabel('Marks')
            ax.set_title(f'Box Plot of Student Marks - {section} Section')

            plt.show()
        except FileNotFoundError:
            print("File not found.")

    def run(self):
        self.root.mainloop()

app = DataAnalysisApp()
app.run()