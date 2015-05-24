from functools import wraps

def memo(f):
    cache = {}
 
    @wraps(f)
    def inner(*args, **kwargs):
        key = str(args) + str(kwargs)
        try:
            return cache[key]
        except KeyError:
            cache[key] = f(*args, **kwargs)
            return cache[key]
    return inner

@memo
def rabbit(n, k):
    if n <= 2:
        return 1
    return k*rabbit(n - 2, k) + rabbit(n - 1, k)

@memo
def mortal(n, m):
    if n < 0:
        return 0
    if n < 2:
        return 1
    return mortal(n - 1, m) + mortal(n - 2, m) - mortal(n - m, m)

for x in range(10):
    print x, mortal(x,3)

print mortal(97,20)
