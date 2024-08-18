n,m = map(int,input().split())
a = [list(map(int,input().split())) for i in range(n)]
for i in range(n):
    for j in range(m):
        if j==0 and i!=0:
            a[i][j]+=a[i-1][j]
        if i==0 and j!=0:
            a[i][j]+=a[i][j-1]
        if i>0 and j>0:
            a[i][j]=min(a[i-1][j],a[i][j-1])+a[i][j]
print(a[n-1][m-1])