import random
n = [random.randint(10**13, 10**13+10000) for i in range(1000)]
c = [0]*10001
for elem in n:
    c[elem - 10**13] += 1

for i in range(len(c)):
    for j in range(c[i]):
        print(i, end=" ")
