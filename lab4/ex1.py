n=int(input("Введіть кількість членів одновимірного масиву: "))
print(f"Введіть {n} елементів масиву:")
count=0
s=0
arr=[int(input()) for _ in range(n)]
for i in range(n):
    if arr[i] < 0:
        s+=arr[i]
        count+=1
if count==0:
    print("У масиві відсутні від'ємні елементи")
else:
    print("Середнє арифметичне від'ємних чисел масиву:", s/count)