n = int(input())
data = list(map(int, input().split()))
data1 = [0]
prev = []
for i in data:
    data1.append(i)

data2 = [data1[0], data1[1]]
for i in range(2, len(data1)):
    if data2[i - 1] < data2[i - 2]:
        data2.append(data2[i - 1] + data1[i])
        prev.append(i - 1)
    else:
        data2.append(data2[i - 2] + data1[i])
        prev.append(i - 2)


print(data2[n], prev)


print(n, end=" ")
k = prev[-1]
while k != 0:
    print(k, end=" ")
    k = prev[k-2]
print(k)
