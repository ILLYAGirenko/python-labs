def seq_search():
    arr=[3, 7, 1, 10, 0, 5, 8, 4, 9, 2, 6, 7, 0, 3, 10, 1, 8, 5, 2, 9]
    seq=list(map(int,input('Введіть послідовність чисел для пошуку у списку (кожен елемент від 0 до 10): ').split()))
    found=0
    for i in range (len(arr)):
        if arr[i:i+len(seq)]==seq:
            print(arr[i:i+len(seq)])
            found=1
            break
    if found==0:
        print("Послідовність не знайдено у списку")
    else:
        print("Послідовність знайдено у списку")
seq_search()