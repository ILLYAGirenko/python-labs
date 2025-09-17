N=int(input("Введіть число N: "))
while N<=1 or N>=9:
    N = int(input("Введіть число N, що лежить між 1  і 9: "))
for i in range(1, N+1):
    for j in range(0, N, 1):
        if j<i:
            print("*", end="")
        else:
            print(" ", end="")
    print(" ")