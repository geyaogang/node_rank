import csv
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def read_csv(filename):
    matrix = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            matrix.append(list(map(float, row)))
    return matrix

def normalize(matrix):
    normalized_matrix = []
    for row in matrix:
        total = sum(row)
        normalized_row = [element / total for element in row]
        normalized_matrix.append(normalized_row)
    return normalized_matrix

def write_csv(filename, matrix):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(matrix)

def select_file():
    filename = filedialog.askopenfilename(title="选择CSV文件", filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
    if filename:
        entry_filename.delete(0, tk.END)
        entry_filename.insert(0, filename)

def normalize_and_save():
    input_filename = entry_filename.get()
    
     # 读取CSV文件
    if not input_filename.endswith(".csv"):
          messagebox.showwarning("无效的文件类型", "请选择一个有效的CSV文件")
          return
    
    try: 
       matrix= read_csv(input_filename)  
    except Exception as e :
           messagebox.showerror("错误","无法读取CSV 文件:\n" + str(e))
           return
        
      # 归一化矩阵
    try: 
          normalized_matrix=normalize(matrix)  
        #   normalized_matrix = [[round(element, 3) for element in row] for row in normalize(matrix)] #保留3位小数
    except Exception as e :
             messagebox.showerror("错误","归一化过程中出错:\n" + str(e))
             return
        
       # 选择保存文件的路径
    output_filename = filedialog.asksaveasfilename(title="保存归一化后的CSV文件", defaultextension=".csv", filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
    if not output_filename:
           return
    
       # 将归一化后的矩阵写入新的CSV文件
    try:
          write_csv(output_filename, normalized_matrix)
          messagebox.showinfo("成功","归一化完成并已存储到" +output_filename+ "中。")
    except Exception as e :
            messagebox.showerror("错误","无法保存归一化后的数据:\n" + str(e))

# 创建UI界面
root = tk.Tk()
root.title("矩阵归一化程序")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label_file = tk.Label(frame, text="选择要处理的CSV文件:")
label_file.grid(row=0, column=0)

entry_filename = tk.Entry(frame)
entry_filename.grid(row=0, column=1)

button_browse = tk.Button(frame, text="浏览...", command=select_file)
button_browse.grid(row=0, column=2)

button_normalize_save = tk.Button(frame, text="归一化并保存", command=normalize_and_save)
button_normalize_save.grid(row=1, columnspan=3)

root.mainloop()