def file_error_check(e):
    #Гиренко: функція для обробки виключних ситуацій при роботі з файлами, що виводить повідомлення у разі помилки при роботі з файлами
    if isinstance(e, FileNotFoundError):
        print("Помилка: файл не знайдено.")
    elif isinstance(e, PermissionError):
        print("Помилка: немає прав для доступу до файлу.")
    elif isinstance(e, IOError):
        print("Помилка вводу/виводу при роботі з файлом.")
    else:
        print(f"Невідома помилка: {e}")

def file_create_and_answer1():
    #Гиренко: функція створює новий файл, з яким будуть працювати всі наступні члени команди, та записує питання для наступного студента
    try:
        #створюємо новий файл для роботи з можливістю редагування та підтримкою кирилиці
        with open("team_file.txt", "w", encoding="utf-8") as file:
            file.write("Студент 1: Гиренко Ілля\n")
            file.write("Чому при роботі з файлами в Python критично важливо використовувати блоки try...except?\n\n")
        print("Студент 1: Файл створено та записано питання.")
    except Exception as e:
        # При виникненні помилки викликаємо наш обробник 'file_error_check'
        file_error_check(e)

file_create_and_answer1()