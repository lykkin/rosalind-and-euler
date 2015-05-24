def partition(li):
    pivot = li.pop(0)
    return pivot, [x for x in li if x < pivot] + [x for x in li if x == pivot] + [pivot] + [x for x in li if x > pivot]


def test(li, pivot):
    flag = -1
    res = True
    for x in li:
        if x == pivot:
            flag = 0
        if x > pivot:
            flag = 1

        if flag == -1:
            res = res and x < pivot
        elif flag == 0:
            res = res and x == pivot
        else:
            res = res and x > pivot
    return res

pivot, li = partition([4, 5, 6, 4, 1, 2, 5, 7, 4])

print li
print test(li, pivot)

f = open('rosalind_par3.txt')
o = open('output.txt', 'w')
f.readline()
pivot, li = partition(map(int, f.readline().split(' ')))
print test(li, pivot)
o.write(' '.join(map(str, li)))
