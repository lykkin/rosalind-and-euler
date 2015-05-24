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
def possibleSums(n):
    if n == 0:
        return 1
    denoms = [1, 2, 5, 10, 20, 50, 100]
    sum = 0
    for denom in denoms:
        if n - denom < 0:
            break
        sum += possibleSums(n - denom)
    return sum

print possibleSums(200)
