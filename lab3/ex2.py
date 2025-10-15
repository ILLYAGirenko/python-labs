a=str(input("Задайте слово, в якому є дві і більше однакові літери: "))
b=""
for i in range(len(a)):
    if a.count(a[i])>1 and a[i] not in b:
        print(a[i])
        b+=a[i]