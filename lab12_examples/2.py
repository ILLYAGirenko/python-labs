import tkinter as tk
from tkinter import ttk

def calculate():
    try:
        val = float(entry.get())
        res = val * 41.5
        lbl_res.config(text=f"Результат: {res:.2f} UAH")
    except ValueError:
        lbl_res.config(text="Помилка введення")

root = tk.Tk()
root.title("Конвертер")
root.geometry("300x200")

container = ttk.Frame(root, padding=20)
container.pack()

ttk.Label(container, text="Сума USD:").grid(row=0, column=0, sticky="w")
entry = ttk.Entry(container)
entry.grid(row=0, column=1, padx=5)
ttk.Button(container, text="Рахувати", command=calculate).grid(row=1, column=0, columnspan=2, pady=10)
lbl_res = ttk.Label(container, text="0.00 UAH")
lbl_res.grid(row=2, column=0, columnspan=2)

root.mainloop()