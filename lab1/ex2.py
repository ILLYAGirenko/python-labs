a=0
b=1
s=0
for i in range(8):
    print(a,end=' ')
    s+=a
    c=a+b
    a=b
    b=c
print("\nСума чисел:",s)

