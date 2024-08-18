import random
b = 0
n = int(input())
A = list(map(int, input().split()))
for i in range(random.choice(A)):
    for j in range(random.choice(A)):
        if A[i] < A[j] and i > j:
            b += 1
print(b)
