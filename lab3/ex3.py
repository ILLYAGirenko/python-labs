a=str(input("Задайте речення: "))
count=0
for i in a.split():
    if i.startswith("н"):
        count+=1
print("Кількість слів що починаються на н:",count)