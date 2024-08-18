def rec(n):
    if n < 1:
        return
    rec(n - 1)
    
    print(n)



rec(5)