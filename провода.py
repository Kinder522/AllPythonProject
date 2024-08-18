n, k = map(int, input().split())
l = [0 for i in range(n)]
for i in range(n):
    l[i] = int(input())

left = 1
r = max(l)

while r-left>1:
    m = (left + r) // 2
    x =0
    i = 0
    while left * r // m == k:
        print(k)
    elif l[m] > k:
        r = m - 1
    else:
        left = m + 1
