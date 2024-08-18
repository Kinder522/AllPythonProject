n = int(input())
x = 0
if n >= 31:
    print("Нет")
else:
    for i in range(n):
        if i - 1 >= 0:
            x += 1
        if i - 2 >= 0:
            x += 1
        if i - 3 >= 0:
            x += 2
print(x)