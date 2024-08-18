n = int(input())
data = [0,0,0,0]*n
data[1] = 2
data[2] = 4
data[3] = 7
if n == 0:
    print(1)
elif n == 1:
    print(data[1])
elif n == 2:
    print(data[2])
elif n == 3:
    print(data[3])
else:
    for i in range(3,len(data)):
        data[i] = data[i - 1] + data[i - 2] + data[i - 3]


print(data[n]+1)