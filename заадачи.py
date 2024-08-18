n, k = map(int, input().split())
a =list(map(int, input().split()))
for i in sorted(a):
    if i == k:
        print(i)

