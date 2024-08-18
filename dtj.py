data = list(map(int, input().split()))
data2 = []

for i in range(1 ,len(data)):
        element = data[i]
        j = i - 1
        while data[j - 1] > element:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = element

print(data2)