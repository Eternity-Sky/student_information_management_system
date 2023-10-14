import tkinter as tk
from tkinter import ttk
import csv

students = []


def add_student(name, age, gender):
    student = {
        'name': name,
        'age': age,
        'gender': gender
    }
    students.append(student)
    print("学生信息添加成功！")


def search_student(name):
    found_students = []
    for student in students:
        if student['name'] == name:
            found_students.append(student)
    if len(found_students) > 0:
        print("找到以下学生信息:")
        for student in found_students:
            print("姓名:", student['name'])
            print("年龄:", student['age'])
            print("性别:", student['gender'])
    else:
        print("未找到该学生信息。")


def export_students():
    if len(students) == 0:
        print("没有学生信息可以导出。")
        return

    file_path = "students.csv"
    with open(file_path, mode='w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["姓名", "年龄", "性别"])
        for student in students:
            writer.writerow([student['name'], student['age'], student['gender']])
    print("学生信息已成功导出到文件:", file_path)


def add_student_window():
    def on_submit():
        name = name_entry.get()
        age = int(age_entry.get())
        gender = gender_combobox.get()
        add_student(name, age, gender)
        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)
        gender_combobox.set("男")

    window = tk.Toplevel()

    name_label = ttk.Label(window, text="姓名:")
    name_label.grid(column=0, row=0, padx=10, pady=10)
    name_entry = ttk.Entry(window)
    name_entry.grid(column=1, row=0, padx=10, pady=10)

    age_label = ttk.Label(window, text="年龄:")
    age_label.grid(column=0, row=1, padx=10, pady=10)
    age_entry = ttk.Entry(window)
    age_entry.grid(column=1, row=1, padx=10, pady=10)

    gender_label = ttk.Label(window, text="性别:")
    gender_label.grid(column=0, row=2, padx=10, pady=10)
    gender_combobox = ttk.Combobox(window, values=["男", "女"])
    gender_combobox.set("男")
    gender_combobox.grid(column=1, row=2, padx=10, pady=10)

    submit_button = ttk.Button(window, text="提交", command=on_submit)
    submit_button.grid(column=0, row=3, columnspan=2, padx=10, pady=10)


def search_student_window():
    def on_submit():
        name = name_entry.get()
        search_student(name)
        name_entry.delete(0, tk.END)

    window = tk.Toplevel()

    name_label = ttk.Label(window, text="姓名:")
    name_label.grid(column=0, row=0, padx=10, pady=10)
    name_entry = ttk.Entry(window)
    name_entry.grid(column=1, row=0, padx=10, pady=10)

    submit_button = ttk.Button(window, text="查找", command=on_submit)
    submit_button.grid(column=0, row=1, columnspan=2, padx=10, pady=10)


def display_menu():
    print("欢迎使用学生信息管理系统！")
    print("1. 添加学生信息")
    print("2. 查找学生信息")
    print("3. 导出学生信息")
    print("0. 退出系统")


def main():
    root = tk.Tk()

    style = ttk.Style()
    style.configure("TButton", padding=10, font=("Arial", 12))
    style.configure("TLabel", padding=10, font=("Arial", 12))

    add_button = ttk.Button(root, text="添加学生信息", command=add_student_window)
    add_button.pack(padx=10, pady=10)

    search_button = ttk.Button(root, text="查找学生信息", command=search_student_window)
    search_button.pack(padx=10, pady=10)

    export_button = ttk.Button(root, text="导出学生信息", command=export_students)
    export_button.pack(padx=10, pady=10)

    exit_button = ttk.Button(root, text="退出", command=root.quit)
    exit_button.pack(padx=10, pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
