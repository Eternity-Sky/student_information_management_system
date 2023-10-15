import json
import csv
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import simpledialog


def load_data():
    filename = askopenfilename(filetypes=[("JSON Files", "*.json")])
    if filename:
        with open(filename, "r") as file:
            data = json.load(file)
        messagebox.showinfo("成功", "数据加载成功！")
        return data


def save_data(data):
    filename = asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
    if filename:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        messagebox.showinfo("成功", "数据保存成功！")


def export_csv(data):
    filename = asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
    if filename:
        with open(filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["姓名", "年龄", "性别"])
            writer.writeheader()
            writer.writerows(data)
        messagebox.showinfo("成功", "CSV文件导出成功！")


def add_student():
    name = simpledialog.askstring("添加学生信息", "请输入姓名：")
    if not name:
        return
    age = simpledialog.askinteger("添加学生信息", "请输入年龄：")
    if not age:
        return
    gender = simpledialog.askstring("添加学生信息", "请输入性别：")
    if not gender:
        return
    student = {"姓名": name, "年龄": age, "性别": gender}
    data.append(student)
    messagebox.showinfo("成功", "学生信息添加成功！")


def search_student():
    query = simpledialog.askstring("查找学生信息", "请输入学生姓名：")
    if not query:
        return
    result = []
    for student in data:
        if query in student.values():
            result.append(student)
    if not result:
        messagebox.showwarning("查询失败", "未找到符合条件的学生信息！")
    else:
        messagebox.showinfo("查询结果", f"共找到{len(result)}条符合条件的学生信息：\n{result}")


def about():
    messagebox.showinfo("关于", "这是一个学生信息管理系统\n作者：Leaovo-man2\n开源地址：https://github.com/Leaovo-man2"
                                "/student_information_management_system")


def main():
    root = Tk()
    root.title("学生信息管理系统")

    # 创建提示文本
    prompt_label = Label(root, text="请在菜单栏上操作", font=("Arial", 16))
    prompt_label.pack(pady=50)

    menubar = Menu(root)

    file_menu = Menu(menubar, tearoff=0)
    file_menu.add_command(label="加载数据", command=lambda: load_data())
    file_menu.add_command(label="保存数据", command=lambda: save_data(data))
    file_menu.add_command(label="导出为CSV", command=lambda: export_csv(data))
    file_menu.add_separator()
    file_menu.add_command(label="退出", command=root.quit)
    menubar.add_cascade(label="文件", menu=file_menu)

    edit_menu = Menu(menubar, tearoff=0)
    edit_menu.add_command(label="添加学生信息", command=add_student)
    edit_menu.add_command(label="查找学生信息", command=search_student)
    menubar.add_cascade(label="编辑", menu=edit_menu)

    help_menu = Menu(menubar, tearoff=0)
    help_menu.add_command(label="关于", command=about)
    menubar.add_cascade(label="帮助", menu=help_menu)

    root.config(menu=menubar)
    root.mainloop()


data = [{}]

if __name__ == "__main__":
    main()
