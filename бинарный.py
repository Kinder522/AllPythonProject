data = list(map(int, input().split()))
f = int(input())

def binar(data, f):
    low = 0
    high = len(data) - 1
    while low <= high:
        m = (low + high) // 2
        if data[m] == f:
            return m
        elif data[m] > f:
            high = m - 1
        else:
            low = m + 1




print(binar(data,f))


