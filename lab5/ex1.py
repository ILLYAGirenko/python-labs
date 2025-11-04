countries = {
    "Україна": {
        "Площа": "603 548 км²",
        "Населення": "36 млн осіб",
        "Частина світу": "Європа"
    },
    "Франція": {
        "Площа": "551 695 км²",
        "Населення": "68 млн осіб",
        "Частина світу": "Європа"
    },
    "Канада": {
        "Площа": "9 984 670 км²",
        "Населення": "40 млн осіб",
        "Частина світу": "Північна Америка"
    },
    "Бразилія": {
        "Площа": "8 515 767 км²",
        "Населення": "216 млн осіб",
        "Частина світу": "Південна Америка"
    },
    "Китай": {
        "Площа": "9 596 961 км²",
        "Населення": "1,41 млрд осіб",
        "Частина світу": "Азія"
    },
    "Японія": {
        "Площа": "377 975 км²",
        "Населення": "125 млн осіб",
        "Частина світу": "Азія"
    },
    "Єгипет": {
        "Площа": "1 001 449 км²",
        "Населення": "113 млн осіб",
        "Частина світу": "Африка"
    },
    "Австралія": {
        "Площа": "7 692 024 км²",
        "Населення": "27 млн осіб",
        "Частина світу": "Австралія"
    },
    "США": {
        "Площа": "9 833 520 км²",
        "Населення": "341 млн осіб",
        "Частина світу": "Північна Америка"
    },
    "Німеччина": {
        "Площа": "357 588 км²",
        "Населення": "84 млн осіб",
        "Частина світу": "Європа"
    }
}

def output(countries):
    for country, info in countries.items():
        print(f"{country}: {info}")

def add(countries):
    try:
        name=input("Введіть назву країни: ").strip()
        if name in countries:
            print("Така країна вже існує у словнику")
            return
        area=input("Введіть площу: ")
        population=input("Введіть кількість населення: ")
        part=input("Введіть частину світу: ")
        countries[name] = {"Площа": area, "Населення": population, "Частина світу": part}
        print("Країну додано")
    except Exception as error:
        print("Помилка")

def delete(countries):
    try:
        name=input("Введіть країну, яку треба видалити: ")
        del countries[name]
        print("Країну видалено")
    except KeyError as error:
        print("Такої країни немає у словнику")
    except Exception as error:
        print("Невідома помилка")

def sort(countries):
    for country in sorted(countries.keys()):
        print(f"{country}: {countries[country]}")

def africa_asia(countries):
    flag=False
    print("Країни, що знаходяться у Африці або Азії:")
    for country, info in countries.items():
        if info["Частина світу"] == "Африка" or info["Частина світу"] == "Азія":
            print(f"{country}: {info}")
            flag=True
    if not flag:
        print("У заданому словнику відсутні країни з Африки або Азії")

def menu():
    while True:
        print("Оберіть дію для роботи з словником")
        print("1 - Вивести всі записи")
        print("2 - Додати країну до списку")
        print("3 - Видалити країну зі списку")
        print("4 - Вивести відсортований за алфавітом словник")
        print("5 - Вивести країну що знаходять у Африці або Азії")
        print("0 - Вихід")
        choice=input("Обрана дія: ")
        if choice == "1":
            output(countries)
        elif choice == "2":
            add(countries)
        elif choice =="3":
            delete(countries)
        elif choice =="4":
            sort(countries)
        elif choice =="5":
            africa_asia(countries)
        elif choice =="0":
            print("Роботу завершено")
            break
        else: print("Введено неправильне число, спрбуйте ще раз")
menu()