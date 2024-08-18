n,m = map(int,input().split())
a = [list(map(int,input().split())) for i in range(m)]

for i in range(n):
    for j in range(m):
        a[i][j] = (min(a[i+1][j],a[i][j+1])+a[i][j])
print(a[n-1][m-1])