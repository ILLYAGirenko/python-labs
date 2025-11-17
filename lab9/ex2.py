import json
import os

DATA_FILE = "countries.json"
RESULT_FILE = "result.json"

def init_json():
    if not os.path.exists(DATA_FILE):
        sample_data = [
            {"name": "Ukraine", "area": 603700, "population": 40000000, "continent": "Europe"},
            {"name": "Egypt", "area": 1002000, "population": 109000000, "continent": "Africa"},
            {"name": "China", "area": 9597000, "population": 1412000000, "continent": "Asia"},
            {"name": "Germany", "area": 357000, "population": 84000000, "continent": "Europe"},
            {"name": "Kenya", "area": 580000, "population": 55000000, "continent": "Africa"},
            {"name": "Japan", "area": 378000, "population": 124000000, "continent": "Asia"},
            {"name": "USA", "area": 9834000, "population": 331000000, "continent": "North America"},
            {"name": "Brazil", "area": 8516000, "population": 214000000, "continent": "South America"},
            {"name": "Australia", "area": 7692000, "population": 26000000, "continent": "Australia"},
            {"name": "India", "area": 3287000, "population": 1393000000, "continent": "Asia"}
        ]
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(sample_data, f, indent=4)

def load_data():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def show_json():
    data = load_data()
    print("\nВміст JSON-файлу:")
    for item in data:
        print(item)

def add_country():
    name = input("Назва країни: ")
    area = int(input("Площа (км²): "))
    population = int(input("Населення: "))
    continent = input("Континент: ")

    data = load_data()
    data.append({
        "name": name,
        "area": area,
        "population": population,
        "continent": continent
    })
    save_data(data)
    print("Країну успішно додано!")

def delete_country():
    name = input("Введіть назву країни, яку потрібно видалити: ")
    data = load_data()
    new_data = [c for c in data if c["name"].lower() != name.lower()]
    if len(new_data) == len(data):
        print("Такої країни не знайдено.")
    else:
        save_data(new_data)
        print("Країну видалено.")

def search_country():
    field = input("Пошук за полем (name/continent): ").strip().lower()
    value = input("Введіть значення: ").strip().lower()
    data = load_data()
    found = [c for c in data if str(c.get(field, "")).lower() == value]
    if found:
        print("Знайдені записи:")
        for c in found:
            print(c)
    else:
        print("Нічого не знайдено.")

def find_asia_africa():
    data = load_data()
    result = [c for c in data if c["continent"] in ("Asia", "Africa")]
    if result:
        print("\nКраїни, що знаходяться в Азії або Африці:")
        for c in result:
            print(c["name"])
        with open(RESULT_FILE, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=4)
        print("\nРезультат записано у", RESULT_FILE)
    else:
        print("Країн в Азії або Африці немає.")

def menu():
    init_json()

    while True:
        print("\n--- МЕНЮ ---")
        print("1 — Показати JSON")
        print("2 — Додати запис")
        print("3 — Видалити запис")
        print("4 — Пошук")
        print("5 — Завдання: знайти країни в Азії або Африці")
        print("0 — Вихід")
        choice = input("Ваш вибір: ")
        if choice == "1":
            show_json()
        elif choice == "2":
            add_country()
        elif choice == "3":
            delete_country()
        elif choice == "4":
            search_country()
        elif choice == "5":
            find_asia_africa()
        elif choice == "0":
            break
        else:
            print("Неправильний вибір!")
menu()
