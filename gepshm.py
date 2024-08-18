n = int(input())
# data = input()
# data = data.split()
# for i in range(n):
#     data[i] = int(data[i])
u = False
data = list(map(int, input().split()))
for i in range(n -1):
    for j in range(n -1):
        if data[j] < data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]





print(data)



