w = int(input())
h = int(input())
n = int(input())
x = 0
while x//w * x//h < n:
    x += 1
print(x)