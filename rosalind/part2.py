def partition(li):
    pivot = li.pop(0)
    return pivot, [x for x in li if x <= pivot] + [pivot] + [x for x in li if x > pivot]


def test(li, pivot):
    flag = 0
    res = True
    for x in li:
        if x > pivot:
            flag = 1

        if flag == 0:
            res = res and x <= pivot
        else:
            res = res and x > pivot
    return res

f = open('rosalind_par.txt')
o = open('output.txt', 'w')
f.readline()
pivot, li = partition(map(int, f.readline().split(' ')))
print test(li, pivot)
o.write(' '.join(map(str, li)))
