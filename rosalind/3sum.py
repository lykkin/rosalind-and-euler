def find_opposites(li):
    for i in xrange(len(li)):
        for j in xrange(i + 1, len(li)):
            for k in xrange(j + 1, len(li)):
                if li[i] + li[j] + li[k] == 0:
                    return i+1, j+1, k+1
    return -1, None, None

f = open('rosalind_3sum.txt')
f.readline()
for line in f:
    first, second, third = find_opposites(map(int, line.split(' ')))
    print first if second is None else ' '.join(map(str, [first, second, third]))
