
data = list(map(int, input().split()))
data2 = []
for i in range(len(data)-1):

    for j in range(len(data)-1):

        if data[j-1] < data[i-1]:

            data2.insert(0,j)
            data.pop(j)

print(data2)