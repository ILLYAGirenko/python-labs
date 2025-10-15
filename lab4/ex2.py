n=7
arr=[[(i-(n-j-1)+1)*(i>=n-j-1) for i in range(n)] for j in range(n)]
for i in arr:
    print(*i)