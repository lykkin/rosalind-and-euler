def swap(li, i, j):
    print len(li), i, j
    temp = li[i]
    li[i] = li[j]
    li[j] = temp


class max_heap():
    heap = []

    def insert(self, el):
        self.heap += [el]
        self.bubble_up(len(self.heap) - 1)
        return self

    def bubble_up(self, i):
        next = (i - 1) // 2
        while next >= 0 and self.heap[i] > self.heap[next]:
            swap(self.heap, i, next)
            i = next
            next = (i - 1) // 2
        return self

    def remove_max(self):
        current_idx = 0
        children = [1, 2]
        while children[0] < len(self.heap):
            if children[1] == len(self.heap):
                max_child = children[0]
            else:
                if self.heap[children[0]] > self.heap[children[1]]:
                    max_child = children[0]
                else:
                    max_child = children[1]
            swap(self.heap, max_child, current_idx)
            current_idx = max_child
            children = [current_idx * 2 + 1, current_idx * 2 + 2]
        return self.heap.pop(current_idx)

    def __str__(self):
        return ' '.join(map(str, self.heap))

heap = max_heap()
heap.insert(1).insert(3).insert(5).insert(7).insert(2)
print heap
print heap.remove_max()
print heap
