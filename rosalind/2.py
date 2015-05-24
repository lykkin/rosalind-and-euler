from math import factorial

from functools import wraps
from datetime import datetime
 
 
class Profiler():
    tracking = {}
 
    def time(self, f):
        @wraps(f)
        def inner(*args, **kwargs):
            start = datetime.now()
            res = f(*args, **kwargs)
            try:
                self.tracking[f.__name__]['runtime'] += datetime.now() - start
                self.tracking[f.__name__]['times_run'] += 1
            except KeyError:
                self.tracking[f.__name__] = {
                    'runtime': datetime.now() - start,
                    'times_run': 1
                }
            return res
        return inner
 
 
p = Profiler()

@p.time
def perms(li):
    res = [[li.pop()]]
    for el in li:
        temp = []
        for perm in res:
            for i in range(len(perm)+1):
                perm_copy = perm[:]
                perm_copy.insert(i, el)
                temp.append(perm_copy)
        res = temp[:]
    return res

def swap(li, i, j):
    t = li[i]
    li[i] = li[j]
    li[j] = t

@p.time
def flipperms(li):
    res = []
    for i in range(factorial(len(li))):
        flip = i % (len(li) - 1)
        swap(li, flip, flip+1)
        res.append(li[:])
    return res


for x in range(2, 12):
    flipperms(range(x))
    perms(range(x))
print p.tracking['perms']['runtime'], p.tracking['flipperms']['runtime']
#f.write(str(len(p)))
#f.write('\n'.join(map(lambda x: ' '.join(map(str, x)), p)))
