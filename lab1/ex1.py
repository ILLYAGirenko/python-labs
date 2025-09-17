a=int(input("Введіть а: "))
while a<0:
    a=int(input("Введіть а, що більше нуля:"))
b=int(input("Введіть b: "))
while b<0:
    b=int(input("Введіть b, що більше нуля:"))
if a<b:
    X=a/b+5
elif a>b:
    X=(a*a-b)/b
else:
    X=-5
print("X =",X)