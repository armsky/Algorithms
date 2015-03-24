"""
- A heap is a tree-like structure.
Heaps are arrays for which a[k] <= a[2*k+1] and a[k] <= a[2*k+2] for all k,
counting elements from 0.
- A heap is NOT a sorted structure and can be regarded as partially ordered

min heap: the smallest key is always at the front
max heap: the largest key is always at the front

            Insert      Find Min
Linked List O(1)        O(n)
BST         O(log n)    O(log n)
Binary heap O(log n)    O(log n)

Deleting the min element taks constant time
But then the structure need to be adjusted, need O(log n) time

"""

# A priority queue is common implemented with a heap

# Stack, Queue and Priority queue are abstract data type,
# but Heap is a specific data structure.

def heapsort(a):
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

