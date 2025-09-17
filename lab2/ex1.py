def expression (m):
    z=1/((m+2)**0.5)
    return z
def progression (n):
    a=10
    b=0
    for i in range(n):
        b += a
        a=a+a*0.1
    return b
m=int(input("Введіть число m: "))
while m<=-2:
    m = int(input("Введіть інше число m: "))
print("z =",expression(m))
n=int(input("Введіть кількість днів, що пробіжить спортсмен: "))
while n<0:
    n = int(input("Введіть позитивне число: "))
print("Спортсмен проіжить =",progression(n), "км")