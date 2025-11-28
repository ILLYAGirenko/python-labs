import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Лаб: Tkinter Basic")
root.geometry("300x150")

# Використання Frame для організації простору
frame = ttk.Frame(root, padding=20)
frame.pack()

label = ttk.Label(frame, text="Аналіз бібліотеки Tkinter", font=("Arial", 12))
label.pack(pady=10)

btn = ttk.Button(frame, text="Вихід", command=root.destroy)
btn.pack()

root.mainloop()