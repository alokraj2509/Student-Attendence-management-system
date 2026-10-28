import tkinter as tk
from tkinter import ttk, messagebox
import csv
import matplotlib.pyplot as plt


students = []




def build_student(name, roll_no, class_name, marks, total_days, present_days):

    total = sum(marks)

    
    percentage = total / len(marks)
    average = total / len(marks)

    highest = max(marks)
    lowest = min(marks)

    
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    
    result = "Pass" if all(m >= 33 for m in marks) else "Fail"

    
    attendance = (
        (present_days / total_days) * 100
        if total_days > 0 else 0
    )

    return {
        "name": name,
        "roll_no": roll_no,
        "class": class_name,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "grade": grade,
        "result": result,
        "total_days": total_days,
        "present_days": present_days,
        "attendance": attendance
    }






sample_data = [
    ("Alok Singh", "101", "10-A", [92, 88, 95, 90, 85], 200, 190),
    ("Shivani Singh", "102", "10-A", [78, 82, 74, 80, 69], 200, 176),
    ("Payal Singh", "103", "10-B", [65, 58, 70, 62, 55], 200, 160),
    ("Sandeep Yadav", "104", "10-B", [88, 91, 84, 79, 93], 200, 195),
    ("Abhishek Singh", "105", "10-C", [45, 30, 52, 48, 40], 200, 140),
    ("Neha Singh", "106", "10-C", [72, 68, 75, 80, 77], 200, 182)
]

for s in sample_data:
    students.append(build_student(*s))




root = tk.Tk()

root.title("Student Performance & Attendance Management System")
root.geometry("1250x750")
root.minsize(1100, 650)





BG_COLOR = "#F4F7FB"
HEADER_COLOR = "#243B55"
SIDEBAR_COLOR = "#1E2A38"
BUTTON_COLOR = "#3498DB"
GREEN_COLOR = "#27AE60"
RED_COLOR = "#E74C3C"
WHITE = "#FFFFFF"
TEXT_COLOR = "#2C3E50"


root.configure(bg=BG_COLOR)





style = ttk.Style()

try:
    style.theme_use("clam")
except:
    pass


style.configure(
    "Treeview",
    background="white",
    foreground=TEXT_COLOR,
    rowheight=30,
    fieldbackground="white",
    font=("Arial", 10)
)

style.configure(
    "Treeview.Heading",
    background=HEADER_COLOR,
    foreground="white",
    font=("Arial", 10, "bold"),
    padding=8
)

style.map(
    "Treeview",
    background=[("selected", "#3498DB")],
    foreground=[("selected", "white")]
)






header = tk.Frame(
    root,
    bg=HEADER_COLOR,
    height=80
)

header.pack(fill="x")
header.pack_propagate(False)


title_label = tk.Label(
    header,
    text="🎓 STUDENT PERFORMANCE & ATTENDANCE SYSTEM",
    bg=HEADER_COLOR,
    fg="white",
    font=("Arial", 20, "bold")
)

title_label.pack(pady=22)






main_frame = tk.Frame(
    root,
    bg=BG_COLOR
)

main_frame.pack(
    fill="both",
    expand=True
)





sidebar = tk.Frame(
    main_frame,
    bg=SIDEBAR_COLOR,
    width=230
)

sidebar.pack(
    side="left",
    fill="y"
)

sidebar.pack_propagate(False)


side_title = tk.Label(
    sidebar,
    text="MENU",
    bg=SIDEBAR_COLOR,
    fg="white",
    font=("Arial", 16, "bold")
)

side_title.pack(pady=(25, 20))




content = tk.Frame(
    main_frame,
    bg=BG_COLOR
)

content.pack(
    side="left",
    fill="both",
    expand=True,
    padx=15,
    pady=15
)






dashboard_frame = tk.Frame(
    content,
    bg=BG_COLOR
)

dashboard_frame.pack(
    fill="both",
    expand=True
)




def clear_content():
    """Remove everything from content area."""

    for widget in content.winfo_children():
        widget.destroy()





def show_dashboard():

    clear_content()

    dashboard_frame = tk.Frame(
        content,
        bg=BG_COLOR
    )

    dashboard_frame.pack(
        fill="both",
        expand=True
    )

    title = tk.Label(
        dashboard_frame,
        text="Dashboard",
        bg=BG_COLOR,
        fg=TEXT_COLOR,
        font=("Arial", 24, "bold")
    )

    title.pack(
        anchor="w",
        pady=(5, 20)
    )


    
    
    
    cards_frame = tk.Frame(
        dashboard_frame,
        bg=BG_COLOR
    )

    cards_frame.pack(
        fill="x"
    )


    total_students = len(students)

    passed = sum(
        1 for s in students
        if s["result"] == "Pass"
    )

    failed = sum(
        1 for s in students
        if s["result"] == "Fail"
    )

    average_percentage = (
        sum(s["percentage"] for s in students)
        / len(students)
        if students else 0
    )


    create_card(
        cards_frame,
        "👨‍🎓",
        "Total Students",
        str(total_students),
        "#3498DB",
        0
    )

    create_card(
        cards_frame,
        "✅",
        "Passed",
        str(passed),
        "#27AE60",
        1
    )

    create_card(
        cards_frame,
        "❌",
        "Failed",
        str(failed),
        "#E74C3C",
        2
    )

    create_card(
        cards_frame,
        "📊",
        "Average %",
        f"{average_percentage:.2f}%",
        "#8E44AD",
        3
    )


    
    
    
    info_frame = tk.Frame(
        dashboard_frame,
        bg="white",
        bd=1,
        relief="solid"
    )

    info_frame.pack(
        fill="both",
        expand=True,
        pady=30
    )


    info_title = tk.Label(
        info_frame,
        text="Student Management System",
        bg="white",
        fg=HEADER_COLOR,
        font=("Arial", 20, "bold")
    )

    info_title.pack(
        pady=(35, 15)
    )


    info_text = (
        "Welcome to the Student Performance & Attendance Management System.\n\n"
        "Use the menu on the left to manage student records.\n\n"
        "• Add new student records\n"
        "• View all students\n"
        "• Search students by roll number\n"
        "• Save data into CSV file\n"
        "• View performance graphs\n"
        "• View attendance graphs"
    )


    info_label = tk.Label(
        info_frame,
        text=info_text,
        bg="white",
        fg=TEXT_COLOR,
        font=("Arial", 12),
        justify="left"
    )

    info_label.pack()






def create_card(parent, icon, title, value, color, column):

    card = tk.Frame(
        parent,
        bg=color,
        width=190,
        height=130
    )

    card.grid(
        row=0,
        column=column,
        padx=8,
        sticky="nsew"
    )

    parent.grid_columnconfigure(
        column,
        weight=1
    )

    card.pack_propagate(False)


    tk.Label(
        card,
        text=icon,
        bg=color,
        fg="white",
        font=("Arial", 24)
    ).pack(
        pady=(12, 2)
    )


    tk.Label(
        card,
        text=title,
        bg=color,
        fg="white",
        font=("Arial", 10, "bold")
    ).pack()


    tk.Label(
        card,
        text=value,
        bg=color,
        fg="white",
        font=("Arial", 20, "bold")
    ).pack(
        pady=5
    )





def add_student_gui():

    clear_content()

    title = tk.Label(
        content,
        text="➕ Add New Student",
        bg=BG_COLOR,
        fg=TEXT_COLOR,
        font=("Arial", 22, "bold")
    )

    title.pack(
        anchor="w",
        pady=(5, 20)
    )


    form = tk.Frame(
        content,
        bg="white",
        bd=1,
        relief="solid"
    )

    form.pack(
        fill="both",
        expand=True
    )


    
    

    name_var = tk.StringVar()
    roll_var = tk.StringVar()
    class_var = tk.StringVar()

    mark_vars = [
        tk.StringVar()
        for _ in range(5)
    ]

    total_days_var = tk.StringVar()
    present_days_var = tk.StringVar()


    
    
    
    def create_entry(label, variable, row):

        tk.Label(
            form,
            text=label,
            bg="white",
            fg=TEXT_COLOR,
            font=("Arial", 11, "bold")
        ).grid(
            row=row,
            column=0,
            padx=25,
            pady=10,
            sticky="w"
        )


        entry = tk.Entry(
            form,
            textvariable=variable,
            font=("Arial", 11),
            width=35,
            bd=1,
            relief="solid"
        )

        entry.grid(
            row=row,
            column=1,
            padx=20,
            pady=10,
            sticky="w"
        )

        return entry


    create_entry(
        "Student Name:",
        name_var,
        0
    )

    create_entry(
        "Roll Number:",
        roll_var,
        1
    )

    create_entry(
        "Class:",
        class_var,
        2
    )


    
    

    marks_title = tk.Label(
        form,
        text="Subject Marks (Out of 100)",
        bg="white",
        fg=HEADER_COLOR,
        font=("Arial", 13, "bold")
    )

    marks_title.grid(
        row=3,
        column=0,
        columnspan=2,
        pady=(15, 5)
    )


    for i in range(5):

        create_entry(
            f"Subject {i + 1}:",
            mark_vars[i],
            i + 4
        )


    create_entry(
        "Total Working Days:",
        total_days_var,
        9
    )

    create_entry(
        "Present Days:",
        present_days_var,
        10
    )


   
    
    
    def save_student():

        name = name_var.get().strip()
        roll_no = roll_var.get().strip()
        class_name = class_var.get().strip()


        if not name or not roll_no or not class_name:

            messagebox.showerror(
                "Error",
                "Please enter Name, Roll Number and Class."
            )

            return


        
        for student in students:

            if student["roll_no"] == roll_no:

                messagebox.showerror(
                    "Error",
                    "Roll number already exists."
                )

                return


        try:

            marks = [
                float(v.get())
                for v in mark_vars
            ]


            for mark in marks:

                if mark < 0 or mark > 100:

                    messagebox.showerror(
                        "Error",
                        "Marks must be between 0 and 100."
                    )

                    return


            total_days = int(
                total_days_var.get()
            )

            present_days = int(
                present_days_var.get()
            )


            if total_days < 0 or present_days < 0:

                raise ValueError


            if present_days > total_days:

                messagebox.showerror(
                    "Error",
                    "Present days cannot be greater than total working days."
                )

                return


        except ValueError:

            messagebox.showerror(
                "Error",
                "Please enter valid numeric values."
            )

            return


        student = build_student(
            name,
            roll_no,
            class_name,
            marks,
            total_days,
            present_days
        )


        students.append(student)


        messagebox.showinfo(
            "Success",
            "Student added successfully!"
        )


        clear_form()


        show_students()


    
    
    
    def clear_form():

        name_var.set("")
        roll_var.set("")
        class_var.set("")

        for variable in mark_vars:
            variable.set("")

        total_days_var.set("")
        present_days_var.set("")


    
    

    button_frame = tk.Frame(
        form,
        bg="white"
    )

    button_frame.grid(
        row=11,
        column=0,
        columnspan=2,
        pady=25
    )


    tk.Button(
        button_frame,
        text="➕ Add Student",
        command=save_student,
        bg=GREEN_COLOR,
        fg="white",
        font=("Arial", 11, "bold"),
        padx=20,
        pady=8,
        bd=0,
        cursor="hand2"
    ).pack(
        side="left",
        padx=10
    )


    tk.Button(
        button_frame,
        text="🧹 Clear",
        command=clear_form,
        bg="#95A5A6",
        fg="white",
        font=("Arial", 11, "bold"),
        padx=25,
        pady=8,
        bd=0,
        cursor="hand2"
    ).pack(
        side="left",
        padx=10
    )





def show_students():

    clear_content()


    title = tk.Label(
        content,
        text="📋 All Student Records",
        bg=BG_COLOR,
        fg=TEXT_COLOR,
        font=("Arial", 22, "bold")
    )

    title.pack(
        anchor="w",
        pady=(5, 15)
    )


    table_frame = tk.Frame(
        content,
        bg="white"
    )

    table_frame.pack(
        fill="both",
        expand=True
    )


    columns = (
        "Name",
        "Roll",
        "Class",
        "Total",
        "Percentage",
        "Average",
        "Highest",
        "Lowest",
        "Grade",
        "Result",
        "Attendance"
    )


    tree = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings"
    )


    for column in columns:

        tree.heading(
            column,
            text=column
        )

        tree.column(
            column,
            width=100,
            anchor="center"
        )


    tree.column(
        "Name",
        width=150
    )


    tree.pack(
        side="left",
        fill="both",
        expand=True
    )


    scrollbar = ttk.Scrollbar(
        table_frame,
        orient="vertical",
        command=tree.yview
    )

    scrollbar.pack(
        side="right",
        fill="y"
    )


    tree.configure(
        yscrollcommand=scrollbar.set
    )




    for student in students:

        tree.insert(
            "",
            "end",
            values=(
                student["name"],
                student["roll_no"],
                student["class"],
                student["total"],
                f"{student['percentage']:.2f}%",
                f"{student['average']:.2f}",
                student["highest"],
                student["lowest"],
                student["grade"],
                student["result"],
                f"{student['attendance']:.2f}%"
            )
        )






def search_student_gui():

    clear_content()


    title = tk.Label(
        content,
        text="🔍 Search Student",
        bg=BG_COLOR,
        fg=TEXT_COLOR,
        font=("Arial", 22, "bold")
    )

    title.pack(
        anchor="w",
        pady=(5, 20)
    )


    search_frame = tk.Frame(
        content,
        bg="white",
        padx=30,
        pady=30
    )

    search_frame.pack(
        fill="x"
    )


    roll_var = tk.StringVar()


    tk.Label(
        search_frame,
        text="Enter Roll Number:",
        bg="white",
        fg=TEXT_COLOR,
        font=("Arial", 12, "bold")
    ).pack(
        side="left"
    )


    entry = tk.Entry(
        search_frame,
        textvariable=roll_var,
        font=("Arial", 12),
        width=25
    )

    entry.pack(
        side="left",
        padx=15
    )


    result_frame = tk.Frame(
        content,
        bg="white"
    )

    result_frame.pack(
        fill="both",
        expand=True,
        pady=20
    )


    def search():

        for widget in result_frame.winfo_children():
            widget.destroy()


        roll = roll_var.get().strip()


        for student in students:

            if student["roll_no"] == roll:

                details = [
                    ("Name", student["name"]),
                    ("Roll Number", student["roll_no"]),
                    ("Class", student["class"]),
                    ("Marks", str(student["marks"])),
                    ("Total Marks", student["total"]),
                    ("Percentage", f"{student['percentage']:.2f}%"),
                    ("Average", f"{student['average']:.2f}"),
                    ("Highest Marks", student["highest"]),
                    ("Lowest Marks", student["lowest"]),
                    ("Grade", student["grade"]),
                    ("Result", student["result"]),
                    ("Total Working Days", student["total_days"]),
                    ("Present Days", student["present_days"]),
                    ("Attendance", f"{student['attendance']:.2f}%")
                ]


                for row, (label, value) in enumerate(details):

                    tk.Label(
                        result_frame,
                        text=label + ":",
                        bg="white",
                        fg=HEADER_COLOR,
                        font=("Arial", 11, "bold")
                    ).grid(
                        row=row,
                        column=0,
                        padx=30,
                        pady=7,
                        sticky="w"
                    )


                    tk.Label(
                        result_frame,
                        text=value,
                        bg="white",
                        fg=TEXT_COLOR,
                        font=("Arial", 11)
                    ).grid(
                        row=row,
                        column=1,
                        padx=30,
                        pady=7,
                        sticky="w"
                    )


                return


        messagebox.showwarning(
            "Not Found",
            "Student not found."
        )


    tk.Button(
        search_frame,
        text="🔍 Search",
        command=search,
        bg=BUTTON_COLOR,
        fg="white",
        font=("Arial", 11, "bold"),
        padx=20,
        pady=7,
        bd=0
    ).pack(
        side="left"
    )





def save_csv_gui():

    if not students:

        messagebox.showwarning(
            "No Data",
            "No student data available."
        )

        return


    with open(
        "student_records.csv",
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)


        writer.writerow([
            "Name",
            "Roll Number",
            "Class",
            "Subject 1",
            "Subject 2",
            "Subject 3",
            "Subject 4",
            "Subject 5",
            "Total",
            "Percentage",
            "Average",
            "Highest",
            "Lowest",
            "Grade",
            "Result",
            "Total Days",
            "Present Days",
            "Attendance"
        ])


        for student in students:

            writer.writerow([
                student["name"],
                student["roll_no"],
                student["class"],
                *student["marks"],
                student["total"],
                round(student["percentage"], 2),
                round(student["average"], 2),
                student["highest"],
                student["lowest"],
                student["grade"],
                student["result"],
                student["total_days"],
                student["present_days"],
                round(student["attendance"], 2)
            ])


    messagebox.showinfo(
        "Success",
        "Student data saved successfully!\n\n"
        "File: student_records.csv"
    )





def performance_graph():

    if not students:

        messagebox.showwarning(
            "No Data",
            "No student data available."
        )

        return


    names = [
        s["name"]
        for s in students
    ]

    percentages = [
        s["percentage"]
        for s in students
    ]


    plt.figure(
        figsize=(10, 6)
    )


    plt.bar(
        names,
        percentages,
        color="steelblue"
    )


    plt.xlabel(
        "Students",
        fontsize=11
    )

    plt.ylabel(
        "Percentage",
        fontsize=11
    )

    plt.title(
        "Student Performance",
        fontsize=15,
        fontweight="bold"
    )


    plt.ylim(
        0,
        100
    )


    plt.xticks(
        rotation=30,
        ha="right"
    )


    plt.grid(
        axis="y",
        linestyle="--",
        alpha=0.3
    )


    plt.tight_layout()

    plt.show()





def attendance_graph():

    if not students:

        messagebox.showwarning(
            "No Data",
            "No student data available."
        )

        return


    names = [
        s["name"]
        for s in students
    ]

    attendance = [
        s["attendance"]
        for s in students
    ]


    plt.figure(
        figsize=(10, 6)
    )


    plt.bar(
        names,
        attendance,
        color="seagreen"
    )


    plt.xlabel(
        "Students",
        fontsize=11
    )

    plt.ylabel(
        "Attendance Percentage",
        fontsize=11
    )

    plt.title(
        "Student Attendance",
        fontsize=15,
        fontweight="bold"
    )


    plt.ylim(
        0,
        100
    )


    plt.xticks(
        rotation=30,
        ha="right"
    )


    plt.grid(
        axis="y",
        linestyle="--",
        alpha=0.3
    )


    plt.tight_layout()

    plt.show()




def sidebar_button(text, command):

    button = tk.Button(
        sidebar,
        text=text,
        command=command,
        bg=SIDEBAR_COLOR,
        fg="white",
        activebackground=BUTTON_COLOR,
        activeforeground="white",
        font=("Arial", 11, "bold"),
        anchor="w",
        padx=25,
        pady=12,
        bd=0,
        cursor="hand2"
    )

    button.pack(
        fill="x",
        padx=10,
        pady=3
    )





sidebar_button(
    "🏠  Dashboard",
    show_dashboard
)

sidebar_button(
    "➕  Add Student",
    add_student_gui
)

sidebar_button(
    "📋  All Students",
    show_students
)

sidebar_button(
    "🔍  Search Student",
    search_student_gui
)

sidebar_button(
    "💾  Save CSV",
    save_csv_gui
)

sidebar_button(
    "📊  Performance Graph",
    performance_graph
)

sidebar_button(
    "📈  Attendance Graph",
    attendance_graph
)





tk.Button(
    sidebar,
    text="❌  Exit",
    command=root.destroy,
    bg=RED_COLOR,
    fg="white",
    activebackground="#C0392B",
    activeforeground="white",
    font=("Arial", 11, "bold"),
    anchor="w",
    padx=25,
    pady=12,
    bd=0,
    cursor="hand2"
).pack(
    side="bottom",
    fill="x",
    padx=10,
    pady=20
)





show_dashboard()

root.mainloop()