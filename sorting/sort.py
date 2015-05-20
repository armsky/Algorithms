# O(n^2), insert first element in unsorted part to the right place of sorted place. Stable, adaptive, and low overhead.
# Time: O(n), O(n^2), O(n^2)
# Space: O(1)
"""
When insertion sort beats quick/merge sort?
Ans: divide-and-conquer has higher overhead.
"""
def insertionSort(aList):
    for i in range(1, len(aList)):
        curValue = aList[i]
        p = i

        while(p > 0 and curValue < aList[p-1]):
            aList[p] = aList[p-1]
            p = p-1
        aList[p] = curValue

# O(n^2), select the minimum from the unsorted part.
# Time: O(n^2), O(n^2), O(n^2)
# Space: O(1)
def selectionSort(aList):
    for i in range(len(aList)):
        minIndex = i
        for j in range(i+1, len(aList)):
            if aList[j] < aList[minIndex]:
                minIndex = j
        if minIndex != i:
            aList[i], aList[minIndex] = aList[minIndex], aList[i]

# O(n^2), stable and adaptive.
# O(n) when the array is almost sorted. Don't chek the array is already sorted on every step.
# Time: O(n), O(n^2), O(n^2)
# Space: O(1)
def bubbleSort(aList):
    swapped = True
    j = 0

    while (swapped):
        swapped = False
        j = j+1
        for i in range(len(aList)-j):
            if aList[i] > aList[i+1]:
                temp = aList[i]
                aList[i] = aList[i+1]
                aList[i+1] = temp
                swapped = True



aList = [21, 2, 45, 103, 0, 64, 0]
insertionSort(aList)
print aList
aList = [21, 2, 45, 103, 0, 64, 0]
selectionSort(aList)
print aList
aList = [21, 2, 45, 103, 0, 64, 0]
bubbleSort(aList)
print aList

