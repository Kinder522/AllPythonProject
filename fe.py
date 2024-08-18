a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
a3, b3= map(int, input().split())
a4, b4= map(int, input().split())
a = a1 + a2 + a3 + a4
b = b1 + b2 + b3 + b4

if a > b:
    print(1)
if a < b:
    print(2)
if a == b:
    print('DRAW')