a = list(map(int, input().split()))

b = list(map(int, input().split()))
dp = [[0]*(len(a)+1) for i in range(len(b)+1)]
for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        if a[i - 1] == b[j - 1]:
            dp[j][i] = dp[j - 1][i - 1] + 1
        else:
            dp[j][i] = max(dp[j][i - 1], dp[j - 1][i])

for i in  range(len(b)+1):
    print(*dp[i])
#1 2 3 4 5 6 7
#3 1 5 4 6 2 7