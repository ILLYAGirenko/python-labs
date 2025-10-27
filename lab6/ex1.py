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

# Функція Мартиненка О. В.
# Функція для редагування даних студента
def edit_student(students):
    name = input("Введіть повне ім'я студента, якого хочете редагувати: ")
    if name not in students:
        print("Студента з таким ім'ям не знайдено.\n")
        return
    student = students[name]
    print(f"\nРедагуємо дані студента: {name}")
    # Зміна групи
    new_group = input(f"Група ({student['Група']}): ")
    if new_group.strip() != "":
        student['Група'] = new_group
    # Зміна курсу
    new_course = input(f"Курс ({student['Курс']}): ")
    if new_course.strip() != "":
        try:
            student['Курс'] = int(new_course)
        except ValueError:
            print("Курс має бути числом. Значення не змінено.")
    # Зміна оцінок по предметах
    subjects = student['Предмети та оцінки за семестр']
    print("\nРедагування предметів та оцінок (залиште порожнім, щоб не змінювати):")
    for subject, grade in subjects.items():
        new_grade = input(f"{subject} ({grade}): ")
        if new_grade.strip() != "":
            try:
                subjects[subject] = int(new_grade)
            except ValueError:
                print(f"Оцінка для предмета '{subject}' має бути числом. Значення не змінено.")
    # Додатково можна додати нові предмети
    while True:
        add_new = input("Додати новий предмет? (так/ні): ").lower()
        if add_new == "ні" or add_new == "":
            break
        elif add_new == "так":
            subject = input("Назва предмета: ")
            try:
                grade = int(input(f"Оцінка з предмета '{subject}': "))
                subjects[subject] = grade
            except ValueError:
                print("Оцінка має бути числом. Предмет не додано.")
    print(f"\nДані студента {name} успішно оновлено!\n")
# Виклик функції
edit_student(students)
