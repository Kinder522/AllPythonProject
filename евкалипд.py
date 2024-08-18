a = int(input())
b = int(input())
c = False
while c == False:
    if a == b:
        c = True
        print("НОД:",a)
    else:
        if a > b:
            a = a - b
        else:
            b = b - a

