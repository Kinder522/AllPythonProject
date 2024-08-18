data =list(map(int, input().split()))
size = 1

def sort(data):
    m = len(data) // 2
    l = data[:m]
    r = data[m:]


    l_half = sort(l)
    r_half = sort(r)

    return merge(l_half, r_half)

def merge(data,data1):
    data2 = []
    i = 0
    j = 0
    while i < len(data) and j < len(data1):
        if data[i] < data1[j]:
            data2.append(data[i])
            i += 1
        else:
            data2.append(data1[j])
            j += 1
    while i < len(data):
        data2.append(data[i])
        i += 1
    while j < len(data1):
        data2.append(data1[j])
        j += 1
    return data2


data3 = sort(data)
print(data3)

