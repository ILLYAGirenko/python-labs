import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Глобальна змінна для збереження датафрейму
df = None

#Функція завантаження CSV файлу: Завантажує CSV файл, перевіряє наявність необхідної колонки '2016 [YR2016]'
#та конвертує дані в числовий формат. Повідомляє користувача про результати операції
def load_csv():
    global df
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if not file_path:
        return
    try:
        df = pd.read_csv(file_path)
        # Перевірка наявності колонки, необхідної для аналізу
        if "2016 [YR2016]" not in df.columns:
            messagebox.showerror("Помилка", "CSV файл повинен містити колонку '2016 [YR2016]'.")
            return
        # Конвертація значень у числовий формат, пропуски перетворюються на NaN
        df["2016 [YR2016]"] = pd.to_numeric(df["2016 [YR2016]"], errors="coerce")
        messagebox.showinfo("Успіх", f"Файл {file_path} було завантажено успішно.")
    except Exception as e:
        # Обробка виключень під час завантаження або читання файлу
        messagebox.showerror("Помилка", f"Не вдалося прочитати файл: {e}")


#Функція аналізу для однієї країни: виконує пошук GDP per capita для заданої країни у 2016 році,
#виводить результат у текстове поле та зберігає його у зовнішньому файлі.
def analyze_country():
    global df
    if df is None:
        messagebox.showerror("Помилка", "Необхідно завантажити CSV файл перед аналізом.")
        return
    country = country_var.get()
    # Перевірка наявності країни у даних
    if country not in df["Country Name"].values:
        messagebox.showerror("Помилка", f"Країна '{country}' не знайдена у наборі даних.")
        return
    gdp_val = df.loc[df["Country Name"] == country, "2016 [YR2016]"].values[0]
    result_text.delete(1.0, tk.END)
    if pd.isna(gdp_val):
        result = f"Дані для країни {country} у 2016 році відсутні."
    else:
        result = f"GDP per capita для країни {country} у 2016 році: {gdp_val:.2f} USD."
    # Вивід результату у графічний інтерфейс
    result_text.insert(tk.END, result)
    # Збереження результату у текстовий файл
    try:
        with open("country_result.txt", "w", encoding="utf-8") as f:
            f.write(result)
        messagebox.showinfo("Збережено", "Результат збережено у файлі country_result.txt.")
    except Exception:
        messagebox.showerror("Помилка", "Не вдалося зберегти файл country_result.txt.")


# Функція аналізу топ-N країн: Формує таблицю топ-N країн за GDP per capita у 2016 році,
#     виводить результати у текстове поле, зберігає таблицю та будує графік
def analyze_top():
    global df
    if df is None:
        messagebox.showerror("Помилка", "Необхідно завантажити CSV файл перед аналізом.")
        return
    # Перетворення введеного значення топ-N у ціле число
    try:
        top_n = int(top_var.get())
    except ValueError:
        messagebox.showerror("Помилка", "Необхідно ввести ціле число для Top N.")
        return
    # Вибірка топ-N країн за значенням GDP per capita
    try:
        df_sorted = df[["Country Name", "2016 [YR2016]"]].dropna().sort_values("2016 [YR2016]", ascending=False).head(top_n)
    except Exception as e:
        messagebox.showerror("Помилка", f"Не вдалося сформувати топ: {e}")
        return
    # Вивід таблиці у текстове поле
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"Топ-{top_n} країн по GDP per capita у 2016 році:\n\n")
    result_text.insert(tk.END, df_sorted.to_string(index=False))
    # Збереження таблиці у зовнішній текстовий файл
    try:
        with open("top_countries.txt", "w", encoding="utf-8") as f:
            f.write(df_sorted.to_string(index=False))
    except Exception:
        messagebox.showerror("Помилка", "Не вдалося зберегти файл top_countries.txt.")
    # Побудова графіка топ-N країн
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(df_sorted["Country Name"], df_sorted["2016 [YR2016]"], color="green")
    ax.set_title(f"Топ-{top_n} країн по GDP per capita (2016)")
    ax.set_ylabel("USD")
    ax.set_xticklabels(df_sorted["Country Name"], rotation=45, ha="right")
    ax.grid(axis="y")
    fig.subplots_adjust(bottom=0.25)
    # Вставка графіка у GUI
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().grid(row=6, column=0, columnspan=3, pady=12)
    # Збереження графіка у зовнішньому файлі
    try:
        fig.savefig("top_plot.png")
        messagebox.showinfo("Збережено", "Таблиця та графік збережено (top_countries.txt, top_plot.png).")
    except Exception:
        messagebox.showerror("Помилка", "Не вдалося зберегти файл графіка top_plot.png.")


#Графічний інтерфейс користувача
window = tk.Tk()
window.title("Аналіз GDP per capita 2016")
# Кнопка для завантаження CSV файлу
tk.Button(window, text="Завантажити CSV", command=load_csv).grid(row=0, column=0, padx=10, pady=10)
# Введення назви країни для аналізу
country_var = tk.StringVar()
tk.Label(window, text="Країна: ").grid(row=1, column=0)
tk.Entry(window, textvariable=country_var).grid(row=1, column=1)
tk.Button(window, text="Показати GDP", command=analyze_country).grid(row=1, column=2)
# Введення параметра Top N для аналізу
top_var = tk.StringVar()
tk.Label(window, text="Топ N: ").grid(row=2, column=0)
tk.Entry(window, textvariable=top_var).grid(row=2, column=1)
tk.Button(window, text="Показати топ", command=analyze_top).grid(row=2, column=2)
# Текстове поле для виводу результатів
result_text = tk.Text(window, width=70, height=12)
result_text.grid(row=4, column=0, columnspan=3, padx=10, pady=10)
# Запуск основного циклу GUI
window.mainloop()
