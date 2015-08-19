def even_fib(limit):
    a, b = 0, 1
    while a < limit:
        if a%2==0:         
            yield a
        a, b = b, a + b
        
print(sum(even_fib(4*10**6)))
