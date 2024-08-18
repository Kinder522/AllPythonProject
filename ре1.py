def a(n):
    a1 = 1
    a2 = 1
    if n == 1 or n == 2:
        return 1
    else:
        return a(n-1) + a(n-2)



n = int(input())
print(a(n))