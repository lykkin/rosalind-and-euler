def find_opposites(li):
    for i in xrange(len(li)):
        for j in xrange(i + 1, len(li)):
            if li[i] == -li[j]:
                return i+1, j+1
    return -1, None

f = open('rosalind_2sum.txt')
f.readline()
for line in f:
    first, second = find_opposites(map(int, line.split(' ')))
    print first if second is None else ' '.join(map(str, [first, second]))
