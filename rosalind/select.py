def partition(li):
    return [x for x in li if x < li[0]], [x for x in li if x > li[0]]


def select(li, k):
    lesser, greater = partition(li)
    if k < len(lesser):
        return select(lesser, k)
    elif k > len(li) - len(greater):
        return select(greater, k - (len(li) - len(greater)))
    else:
        return li[0]

f = open('rosalind_med.txt')
f.readline()
li = map(int, f.readline().split(' '))
k = int(f.readline())
print select(li, k)
