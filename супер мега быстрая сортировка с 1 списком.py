import random
data = list(map(int, input().split()))
fst = data[0]
lst = data[-1]
def quicksort(A, l, r):
    if l >= r:
        return
    else:
        q = random.choice(A[l:r + 1])
        i = l
        j = r
        while i <= j:
            while A[i] < q:
                i += 1
            while A[j] > q:
                j -= 1
            if i <= j:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
        quicksort(A, l, j)
        quicksort(A, i, r)

quicksort(data,0,len(data)-1)
print(data)


