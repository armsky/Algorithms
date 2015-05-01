"""
- A heap is a tree-like structure.
Heaps are arrays for which a[k] <= a[2*k+1] and a[k] <= a[2*k+2] for all k,
counting elements from 0.
- A heap is NOT a sorted structure and can be regarded as partially ordered

min heap: the smallest key is always at the front
max heap: the largest key is always at the front

Time        Insert      Find Min
Linked List O(1)        O(n)
BST         O(log n)    O(log n)
Binary heap O(log n)    O(log n)

Deleting the min element takes constant time
But then the structure need to be adjusted, need O(log n) time
Not adaptive
"""

# A priority queue is common implemented with a heap

# Stack, Queue and Priority queue are abstract data type,
# but Heap is a specific data structure.
def heapsort(a):
    def heapify(a):
        start = len(a)/2 -1
        while start >= 0:
            sift(start, len(a))
            start -= 1

    def sift(root, n):
        while root*2 + 1 < n:
            child = root*2 + 1
            if child < n-1 and a[child] < a[child+1]:
                child += 1
            if a[root] < a[child]:
                a[root], a[child] = a[child], a[root]
                root = child
            else:
                return
    heapify(a)
    print a
    print "###"
    end = len(a)-1
    while end > 0:
        # Swap the largest element to the end
        a[end], a[0] = a[0], a[end]
        print a
        sift(0, end)
        end -= 1

def heapsort_recursive(a):
    def swap(a, i, j):
       a[i], a[j] = a[j], a[i]

    def siftdown(a, i, size):
        left = 2*i +1
        right = 2*i +2
        largest = i

        if left < size-1 and a[left] > a[i]:
            largest = left
        if right < size-1 and a[right] > a[largest]:
            largest = right
        if largest != i:
            swap(a, i, largest)
            siftdown(a, largest, size)

    # a bottom-up manner
    def heapify(a, size):
        p = size/2 - 1
        while p >= 0:
            siftdown(a, p, size)
            p -= 1

    size = len(a)
    heapify(a, size)
    end = size - 1
    while end > 0:
        swap(a, 0, end)
        siftdown(a, 0, end)
        end -= 1

def min_heapify(a):
    def sift(a, i, n):
        l = 2*i +1
        r = 2*i +2
        sm = i
        if l < n-1 and a[l] < a[i]:
            sm = l
        if r < n-1 and a[r] < a[sm]:
            sm = r
        if sm != i:
            a[i], a[sm] = a[sm], a[i]
            sift(a, sm, n)

    def heapify(a, size):
        p = size/2 - 1
        while p >= 0:
            sift(a, p, size)
            p -= 1

    n = len(a)
    heapify(a, n)
    end = n - 1
    while end > 0:
        sift(a, 0, end)
        end -= 1


a = [100,-10,-8,0,1,3,11,35,68,500]
#min_heapify(a)
heapsort(a)
print a
