def maj(li):
    counts = {}
    for el in li:
        try:
            counts[el] += 1
        except KeyError:
            counts[el] = 1
    res = sorted(counts.iteritems(), reverse=True, key=lambda (k,v): v)[0]
    return res[0] if res[1] > len(li)/2 else -1


f = open('rosalind_maj.txt')
f.readline()
res = []
for line in f:
    res += [maj(line.split(' '))]

print ' '.join(map(str, res))
