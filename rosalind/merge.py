def merge(li1, li2):
    res = []
    while li1 and li2:
        if li1[0] < li2[0]:
            res += [li1.pop(0)]
        else:
            res += [li2.pop(0)]
    if li1:
        res += li1
    if li2:
        res += li2
    return res


f = open('rosalind_mer.txt')
o = open('ozxicjvoixcjvoixcvj', 'w')
f.readline()
li1 = map(int, f.readline().split(' '))
f.readline()
li2 = map(int, f.readline().split(' '))
o.write(' '.join(map(str, merge(li1,li2))))
