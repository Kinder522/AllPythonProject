n, k = map(int, input().split())
data = list(map(int, input().split()))
data = sorted(data)
x = 1
for i in range(len(data)):
    if k == data[i]:
        print(x)
    else:
        x += 1
