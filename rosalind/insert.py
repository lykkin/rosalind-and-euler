def swap(li, i, j):
    temp = li[i]
    li[i] = li[j]
    li[j] = temp

def insert(li):
    res = li[:]
    swaps = 0
    for i in xrange(1, len(li)):
        k = i
        while k > 0 and li[k] < li[k-1]:
            swap(li, k-1, k)
            swaps += 1
            k -= 1

    return swaps

f = open('rosalind_ins.txt')
f.readline()
li = map(int, f.readline()[:-1].split(' '))
print li
print insert(li)
print li
