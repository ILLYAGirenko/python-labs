def val_insert():
    arr=list(map(int,input('Введіть список: ').split()))
    print(arr)
    k = int(input('Введіть індекс числа: '))
    a=int(input('Введіть число, що буде вставлено у обрану позицію: '))
    arr.insert(k,a)
    print("Оновлений список: ",arr)
val_insert()

