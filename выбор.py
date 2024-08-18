data =list(map(int, input().split()))
for i in range(len(data)):
    min = i
    for j in range(i + 1,len(data)):
        if data[j] < data[min]:
            min = j
    data[i], data[min] = data[min], data[i]
print(data)
#операций:5+(data+1)*(data+2+1)+2+1=8+2data+(data+2)+(data+1) Онатаций:n=O(n^2)

