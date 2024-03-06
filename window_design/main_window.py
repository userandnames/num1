from tkinter import *
import os
import re


class MainWindow():
    def __init__(self):
        self.root = Tk()
        self.root.title("111")
        self.root.geometry("500x600")

        self.work_path = os.getcwd().replace(os.path.basename(os.getcwd()), "save")
        self.saved_list = os.listdir(self.work_path)

        self.List1 = Listbox(self.root)
        self.label = Label(self.root)
        self.button = Button(self.root, text="执行")

    @staticmethod
    def on_item_click(label1, event):
        index = event.widget.curselection()[0]  # 获取当前选中项的索引
        value = event.widget.get(index)  # 获取选中项的值
        label1.config(text=f"Clicked: {value}")

    def rename_item(self, index, entry, text):
        # 获取Entry小部件中的文本
        new_text = entry.get()
        # 更新Listbox中的项
        self.List1.delete(index)
        self.List1.insert(index, new_text)
        # 销毁Entry小部件
        entry.destroy()
        for i in self.saved_list:
            base_name, extension = os.path.splitext(i)
            if text == base_name:
                os.rename(self.work_path + "\\" + i, self.work_path + "\\" + new_text + extension)

    def change_names(self, event):
        index = self.List1.nearest(event.y)
        text = self.List1.get(index)
        entry = Entry(self.root)
        entry.insert(0, text)
        entry.place(x=event.x, y=event.y)
        # 绑定回车键事件处理函数
        entry.bind("<Return>", lambda e: self.rename_item(index, entry, text))
        # 绑定失去焦点事件处理函数
        entry.bind("<FocusOut>", lambda e: self.rename_item(index, entry, text))
        # 设置焦点到Entry小部件
        entry.focus_set()

    def insert_saved_files(self, listbox):
        all_files = []
        for i in self.saved_list:
            i = re.sub(r'\.[^.]*$', '', i)
            if i not in all_files:
                all_files.append(i)
        for i in all_files:
            listbox.insert(END, i)

    def packing(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        print(width, height)
        # self.List1.pack()
        self.insert_saved_files(self.List1)
        self.List1.bind("<<ListboxSelect>>", lambda event: self.on_item_click(self.label, event))
        self.List1.bind("<Double-Button-1>", self.change_names)
        self.List1.place(x=0, y=0, width=0.4*width, height=height/3)
        self.label.place(x=0.4*width+50, y=height/6)
        self.button.place(x=0.4*width+50, y=height/6+50)


    def start_work(self):
        self.packing()
        self.root.mainloop()


if __name__ == "__main__":
    app = MainWindow()
    app.start_work()

