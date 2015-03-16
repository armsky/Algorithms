# Merge Sort
def mergeSort(aList):
    if len(aList) <= 1:
        return aList
    else:
        mid = len(aList)/2
        left = mergeSort(aList[0:mid])
        right = mergeSort(aList[mid:])
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
def quickSort(a, left, right):
    i = left
    j = right
    pivot = a[(left + right) / 2]

    while (i <= j):
        while (a[i] < pivot):
            i = i + 1
        while (a[j] > pivot):
            j = j - 1
        if (i <= j):
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
            i = i + 1
            j = j - 1

    if (left < j):
        quickSort(a, left, j)
    if (i < right):
        quickSort(a, i, right)


aList = [21, 2, 45, 103, 0, 64, 0]
print mergeSort(aList)
aList = [21, 2, 45, 103, 0, 64, 0]
quickSort(aList, 0, len(aList)-1)
print aList
