
data = list(map(int, input().split()))
dp = [1]*len(data)
dp[0]=1
prev = []
if len(data) == 1:
    print(dp[0])
else:
    for i in range(len(dp)):
        for j in range(i):
            if data[j] < data[i] and dp[i]<dp[j]+1:
                dp[i] = dp[j] + 1


    print(max(dp))