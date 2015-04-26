# Merge Sort
# divide and conquer
# Time: O(n log n), O(n log n), O(n log n)
# Space: O(n)
def mergesort(aList):
    if len(aList) <= 1:
        return aList
    else:
        mid = len(aList)/2
        left = mergesort(aList[0:mid])
        right = mergesort(aList[mid:])
        # If two sub-list already sorted
        if left[-1] <= right[0]:
            return left + right
        else:
            return merge(left, right)


def merge(left, right):
    result = list()
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            # This works even list has only one element left
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    if len(left) > 0:
        result = result + left
    if len(right) > 0:
        result = result + right
    return result


# Quick sort
# O(n log n), divide-and-conquer, in-place, short inner loop
# Time: O(n log n), O(n log n), O(n^2)
# Space: O(log n)
"""This extra space is used in stack frames, it's not practical for making it
iterative because it's not tail recursive
"""
"""
When is QuickSort impractical?
Ans:
    1. Any situation when you do not have random access in O(1), i.e. Linked list
    2. Distributed sorting. i.e. sort data across files
"""
def quicksort(a, left, right):
    i = left
    j = right
    pivot = a[(left + right) / 2]

    while (i <= j):
        while (a[i] < pivot):
            i = i + 1
        while (a[j] > pivot):
            j = j - 1
        if (i <= j):
            # swap a[i], a[j]
            a[i], a[j] = a[j], a[i]
            i = i + 1
            j = j - 1

    if (left < j):
        quicksort(a, left, j)
    if (i < right):
        quicksort(a, i, right)


# Heapsort
# O(n·lg(n)) in-place sort, but is not stable.
# Heapsort is not stable because operations on the heap can change the relative order of equal items.
# Time: O(n log n), O(n log n), O(n log n)
# Space: O(1)
#* time complexity of building a heap is: O(n)
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

# Radix sort

aList = [21, 2, 45, 103, 0, 64, 0]
print mergesort(aList)
aList = [21, 2, 45, 103, 0, 64, 0]
quicksort(aList, 0, len(aList)-1)
print aList
aList = [21, 2, 45, 103, 0, 64, 0]
heapsort(aList)
print aList
