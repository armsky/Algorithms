# Radix sort


# Counting sort
from collections import defaultdict
def countingSort(array, mn, mx):
    count = defaultdict(int)
    for i in array:
        count[i] += 1
    result = []
    for j in range(mn,mx+1):
        result += [j]* count[j]
    return result



aList = [21, 2, 45, 103, 0, 64, 0]
print mergesort(aList)
aList = [21, 2, 45, 103, 0, 64, 0]
quicksort(aList, 0, len(aList)-1)
print aList
aList = [21, 2, 45, 103, 0, 64, 0]
heapsort(aList)
print aList
