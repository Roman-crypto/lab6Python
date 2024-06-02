import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        x1 = float(entry_x1.get())
        x2 = float(entry_x2.get())
        y = x1 * x2  
        mean = (x1 + x2) / 2
        entry_y.delete(0, tk.END)
        entry_y.insert(0, str(y))
        entry_mean.delete(0, tk.END)
        entry_mean.insert(0, str(mean))
    except ValueError:
        messagebox.showerror("Помилка", "Будь ласка, введіть коректні числові значення.")

def clear():
    entry_x1.delete(0, tk.END)
    entry_x2.delete(0, tk.END)
    entry_y.delete(0, tk.END)
    entry_mean.delete(0, tk.END)

def exit_app():
    root.quit()

root = tk.Tk()
root.title("Лабораторна робота №6")


label_x1 = tk.Label(root, text="Змінна X1")
label_x1.grid(row=0, column=0, padx=10, pady=5)

label_x2 = tk.Label(root, text="Змінна X2")
label_x2.grid(row=1, column=0, padx=10, pady=5)

label_y = tk.Label(root, text="Результат розрахунку Y")
label_y.grid(row=2, column=0, padx=10, pady=5)

label_mean = tk.Label(root, text="Середнє Арифметичне")
label_mean.grid(row=3, column=0, padx=10, pady=5)

entry_x1 = tk.Entry(root)
entry_x1.grid(row=0, column=1, padx=10, pady=5)

entry_x2 = tk.Entry(root)
entry_x2.grid(row=1, column=1, padx=10, pady=5)

entry_y = tk.Entry(root)
entry_y.grid(row=2, column=1, padx=10, pady=5)

entry_mean = tk.Entry(root)
entry_mean.grid(row=3, column=1, padx=10, pady=5)

button_calculate = tk.Button(root, text="Обчислити", command=calculate)
button_calculate.grid(row=4, column=0, padx=10, pady=10)

button_clear = tk.Button(root, text="Очистити", command=clear)
button_clear.grid(row=4, column=1, padx=10, pady=10)

button_exit = tk.Button(root, text="Вихід", command=exit_app)
button_exit.grid(row=4, column=2, padx=10, pady=10)

root.mainloop()

