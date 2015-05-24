from math import floor

def find(i, li, lower, upper):
    midpoint = lower + (upper - lower)//2
    while upper >= lower:
        if li[midpoint] == i:
            return midpoint + 1
        elif li[midpoint] < i:
            lower = midpoint + 1
        else: 
            upper = midpoint - 1
        midpoint = lower + (upper - lower)//2
    return -1

for x in [40,10,35,15,40,20]:
    print find(x, [10,20,30,40,50], 0, 4)

f = open('rosalind_bins.txt')
f.readline()
f.readline()
li = map(int, f.readline().split(' '))
needles = map(int, f.readline().split(' '))

def get(li, x):
    try:
        return li.index(x) + 1
    except:
        return -1

for n in needles:
    find_idx = find(n, li, 0, len(li) - 1)
    get_idx = get(li, n)
    if find_idx != get_idx:
        print 'no match on %s, bins: (%s, %s), list.index: (%s, %s)' % (n, find_idx, li[find_idx - 1], get_idx, li[get_idx - 1])
        print li[find_idx - 1], li[get_idx - 1]
        if li[find_idx - 1] == n:
            print 'bins right'
        if li[get_idx - 1] == n:
            print 'index right'

#li = filter(lambda (x, y, n): x != y, zip(map(lambda x: find(x, li, 0, len(li) - 1), needles), map(lambda x: get(li, x), needles), needles))
#for x, y, n in li:
#    print x, y, x+1

o = open('ahhhhh', 'w')
o.write(' '.join(map(lambda x: str(find(x, li, 0, len(li) - 1)), needles)))
