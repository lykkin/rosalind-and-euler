def find_opposites(li):
    sums = {}

    for i in xrange(len(li)):
        sums[li[i]] = i

    for i in xrange(len(li)):
        for j in xrange(i + 1, len(li)):
            try:
                res = [i, j, sums[-(li[i] + li[j])]]
                print res, map(lambda x: li[x], res), sum(map(lambda x: li[x], res))
                return res
            except:
                pass
    return -1, None, None

f = open('rosalind_3sum.txt')
f.readline()
for line in f:
    first, second, third = find_opposites(map(int, line.split(' ')))
    print first if second is None else ' '.join(map(str, [first, second, third]))
