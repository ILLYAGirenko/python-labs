import csv

try:
    with open("Data.csv", "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        print("Country Name: 2016 [YR2016]\n")
        for row in reader:
            print(row['Country Name'], ': ', row["2016 [YR2016]"])
except FileNotFoundError:
    print("Файл Data.csv не знайдено!")

try:
    with open("Data.csv", "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        while True:
            inp = input("\nВведіть значення, щоб знайти показники, які більші, ніж значення, яке ви ввели: ")
            try:
                indicator = float(inp)
                break
            except ValueError:
                print("Введіть число!")
        flag = False
        print("\nCountry Name: 2016 [YR2016]\n")
        with open("new_Data.csv", "w", encoding="utf-8", newline="") as out:
            writer = csv.writer(out)
            writer.writerow(["Country Name", "2016 [YR2016]"])
            for row in reader:
                try:
                    value = float(row["2016 [YR2016]"])
                except:
                    continue
                if value > indicator:
                    flag = True
                    print(row["Country Name"], ": ", value)
                    writer.writerow([row["Country Name"], value])
        if not flag:
            print(f"Показників, більших за {indicator}, немає.")
except FileNotFoundError:
    print("Файл Data.csv не знайдено!")
