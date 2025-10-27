#Створення словника
students={
    "Гиренко Ілля Романович":{
        'Група': "КН41/1",
        'Курс':1,
        'Предмети та оцінки за семестр':{
            "Вища математика":80,
            "Програмування":81,
            "Дискретна математика":85
        }
    },
    "Мартиненко Олександр Володимирович":{
            'Група': "КН41/1",
            'Курс':1,
            'Предмети та оцінки за семестр':{
                "Вища математика":83,
                "Програмування":82,
                "Дискретна математика":84
            }
        },
    "Репін Данііл Вікторович":{
            'Група': "КН41/1",
            'Курс':1,
            'Предмети та оцінки за семестр':{
                "Вища математика":89,
                "Програмування":80,
                "Дискретна математика":87
            }
        },
    "Спічаков Павло Ігорович":{
            'Група': "КН41/1",
            'Курс':1,
            'Предмети та оцінки за семестр':{
                "Вища математика":80,
                "Програмування":90,
                "Дискретна математика":82
            }
        }
}

#Функція Гиренка І. Р.
#Додавання нового студента до словника
def add_student(students):
    name=input("Введіть повне ім'я нового студента: ")
    group=input("Введіть групу студента: ")
    course=int(input("Введіть курс студента: "))
    subjects={}
    print("\nВведіть предмети та оцінки за семестр (для завершення введення введіть порожню назву\n")
    while True:
        subject=input("Назва предмета: ")
        if subject == "":
            break
        try:
            grade = int(input(f"Оцінка з предмета '{subject}': "))
        except ValueError:
            print("Будь ласка, введіть числове значення оцінки.")
            continue
        subjects[subject] = grade
    students[name] = {
            "Група": group,
            "Курс": course,
            "Предмети та оцінки за семестр": subjects
    }
    print("Студента {name} успішно додано!\n")

add_student(students)

#функція Репіна Д. В.
#Редагування оцінок студента
def edit_student_grade(students):
    name = input("Введіть повне ім'я студента для редагування: ")
    if name in students:
        print("Поточні оцінки:")
        for subj, grade in students[name]["Предмети та оцінки за семестр"].items():
            print(f"{subj}: {grade}")
        subject = input("Введіть предмет, який потрібно змінити: ")
        if subject in students[name]["Предмети та оцінки за семестр"]:
            try:
                new_grade = int(input("Нова оцінка: "))
                students[name]["Предмети та оцінки за семестр"][subject] = new_grade
                print("Оцінку успішно змінено!")
            except ValueError:
                print("Помилка: оцінка має бути числом.")
        else:
            print("Такого предмета немає.")
    else:
        print("Студента не знайдено.")

edit_student_grade(students)

#функція Спічаков П.І.
#видалення студентів зі списку
def delete_student(students):
    name = input("Введіть повне ім'я студента для видалення: ")
    if name in students:
        del students[name]
        print(f"Студента {name} успішно видалено.")
    else:
        print("Студента не знайдено.")
delete_student(students)

#функція Мартиненка О.В.
#Пошук студента з найвищим середнім балом
def find_top_student(students):
    best_student = None
    best_avg = 0
    for name, info in students.items():
        grades = info["Предмети та оцінки за семестр"].values()
        if grades:
            avg = sum(grades) / len(grades)
            if avg > best_avg:
                best_avg = avg
                best_student = name
    if best_student:
        print(f"\nНайвищий середній бал має студент: {best_student} ({best_avg:.2f})")
    else:
        print("Немає даних про оцінки.")
find_top_student(students)
