import os
import csv
import json
import tkinter as tk
from tkinter import ttk

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

def save_students(file_path):
    with open(file_path, mode='w') as json_file:
        json.dump(students, json_file)
    print("学生信息已成功保存到文件:", file_path)

def load_students(file_path):
    try:
        with open(file_path, mode='r') as json_file:
            students.extend(json.load(json_file))
        print("成功加载学生信息。")
    except FileNotFoundError:
        print("未找到保存的学生信息文件，将创建新的文件。")

def export_csv(file_path):
    try:
        with open(file_path, mode='w', newline='') as csv_file:
            fieldnames = ['姓名', '年龄', '性别']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for student in students:
                writer.writerow(student)
        print("导出CSV文件成功！")
    except Exception as e:
        print("导出CSV文件失败:", str(e))

def add_student_window():
    window = tk.Toplevel()
    window.title("添加学生信息")
    window.geometry("300x150")

    def add_student_callback():
        name = name_entry.get()
        age = age_entry.get()
        gender = gender_combobox.get()
        add_student(name, age, gender)
        window.destroy()

    name_label = ttk.Label(window, text="姓名：")
    name_label.grid(column=0, row=0, padx=10, pady=10, sticky=tk.W)

    name_entry = ttk.Entry(window, width=20)
    name_entry.grid(column=1, row=0, padx=10, pady=10, sticky=(tk.W, tk.E))

    age_label = ttk.Label(window, text="年龄：")
    age_label.grid(column=0, row=1, padx=10, pady=10, sticky=tk.W)

    age_entry = ttk.Entry(window, width=20)
    age_entry.grid(column=1, row=1, padx=10, pady=10, sticky=(tk.W, tk.E))

    gender_label = ttk.Label(window, text="性别：")
    gender_label.grid(column=0, row=2, padx=10, pady=10, sticky=tk.W)

    gender_combobox = ttk.Combobox(window, values=["男", "女"])
    gender_combobox.grid(column=1, row=2, padx=10, pady=10, sticky=(tk.W, tk.E))

    add_button = ttk.Button(window, text="添加", command=add_student_callback)
    add_button.grid(column=0, row=3, padx=10, pady=10, sticky=tk.W)

    cancel_button = ttk.Button(window, text="取消", command=window.destroy)
    cancel_button.grid(column=1, row=3, padx=10, pady=10, sticky=tk.E)

    name_entry.focus()

def search_student_window():
    window = tk.Toplevel()
    window.title("搜索学生信息")
    window.geometry("300x100")

    def search_student_callback():
        name = name_entry.get()
        search_student(name)
        window.destroy()

    name_label = ttk.Label(window, text="姓名：")
    name_label.grid(column=0, row=0, padx=10, pady=10, sticky=tk.W)

    name_entry = ttk.Entry(window, width=20)
    name_entry.grid(column=1, row=0, padx=10, pady=10, sticky=(tk.W, tk.E))

    search_button = ttk.Button(window, text="搜索", command=search_student_callback)
    search_button.grid(column=0, row=1, padx=10, pady=10, sticky=tk.W)

    cancel_button = ttk.Button(window, text="取消", command=window.destroy)
    cancel_button.grid(column=1, row=1, padx=10, pady=10, sticky=tk.E)

    name_entry.focus()

def display_menu():
    print("\n欢迎使用 学生信息管理系统\n")
    print("请选择要进行的操作：")
    print("1. 添加学生信息")
    print("2. 搜索学生信息")
    print("3. 退出程序")

def main():
    json_file_path = os.path.join("lod", "students.json")
    csv_file_path = os.path.join("lod", "students.csv")
    load_students(json_file_path)

    root = tk.Tk()
    root.title("学生信息管理系统")
    root.geometry("300x100")

    style = ttk.Style(root)
    style.theme_use("clam")

    add_student_button = ttk.Button(root, text="添加学生信息", command=add_student_window)
    add_student_button.pack(side=tk.LEFT, padx=10, pady=10)

    search_student_button = ttk.Button(root, text="搜索学生信息", command=search_student_window)
    search_student_button.pack(side=tk.LEFT, padx=10, pady=10)

    quit_button = ttk.Button(root, text="退出程序", command=root.destroy)
    quit_button.pack(side=tk.LEFT, padx=10, pady=10)

    def save_students_callback():
        save_students(json_file_path)

    def export_csv_callback():
        directory = "exports"
        os.makedirs(directory, exist_ok=True)
        export_file_path = os.path.join(directory, "students.csv")
        export_csv(export_file_path)

    def about_callback():
        print("Github")

    menu_bar = tk.Menu(root)
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="保存加载项", command=save_students_callback)
    file_menu.add_command(label="导出预览", command=export_csv_callback)
    menu_bar.add_cascade(label="文件", menu=file_menu)

    help_menu = tk.Menu(menu_bar, tearoff=0)
    help_menu.add_command(label="关于", command=about_callback)
    menu_bar.add_cascade(label="帮助", menu=help_menu)

    root.config(menu=menu_bar)
    root.protocol("WM_DELETE_WINDOW", save_students_callback)

    root.mainloop()

if __name__ == "__main__":
    main()
