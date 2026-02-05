import tkinter as tk
import random
import time
from tkinter import messagebox

with open("names.txt", "r", encoding="utf-8") as f:
    all_names = [line.strip() for line in f if line.strip()]

remaining_names = all_names.copy()
used_names = []

root = tk.Tk()
root.title("🎉 随机名字抽取系统")
root.geometry("600x400")
root.resizable(False, False)

result_var = tk.StringVar()
result_var.set("请输入抽取人数")

result_label = tk.Label(
    root,
    textvariable=result_var,
    font=("微软雅黑", 28, "bold"),
    fg="blue",
    justify="center"
)
result_label.pack(pady=30)

frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="抽取人数：", font=("微软雅黑", 14)).pack(side="left")

count_entry = tk.Entry(frame, width=5, font=("微软雅黑", 14))
count_entry.insert(0, "1")
count_entry.pack(side="left")

is_running = False

def draw_names():
    global is_running
    if is_running:
        return
    try:
        count = int(count_entry.get())
        if count <= 0:
            raise ValueError
    except:
        messagebox.showerror("错误", "请输入正确的抽取人数")
        return
    if count > len(remaining_names):
        messagebox.showwarning("提示", "剩余人数不足")
        return
    is_running = True
    for _ in range(25):
        temp = random.sample(remaining_names, count)
        result_var.set("\n".join(temp))
        root.update()
        time.sleep(0.05)
    chosen = random.sample(remaining_names, count)
    for name in chosen:
        remaining_names.remove(name)
        used_names.append(name)
    result_var.set("\n".join(chosen))
    is_running = False
    with open("result.txt", "a", encoding="utf-8") as f:
        for name in chosen:
            f.write(name + "\n")

def redraw():
    if not remaining_names:
        result_var.set("🎊 全部抽完啦！")
        return
    draw_names()

btn_frame = tk.Frame(root)
btn_frame.pack(pady=20)

tk.Button(btn_frame, text="🎯 开始抽取", font=("微软雅黑", 14),
          width=12, bg="#4CAF50", fg="white", command=draw_names).pack(side="left", padx=10)

tk.Button(btn_frame, text="🔄 再次抽取", font=("微软雅黑", 14),
          width=12, bg="#2196F3", fg="white", command=redraw).pack(side="left", padx=10)

root.mainloop()