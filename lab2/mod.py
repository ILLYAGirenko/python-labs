def progression (n):
    a=10
    b=0
    for i in range(n):
        b += a
        a=a+a*0.1
    return b