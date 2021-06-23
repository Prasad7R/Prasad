fibdict={0:0,1:1}

def fib(n):
    if n in fibdict:
        return fibdict[n]
    
    res =fib(n-1) + fib(n-2)
    fibdict[n]=res
    print(fibdict)
    return res

fib(5)
print(fibdict.values())
