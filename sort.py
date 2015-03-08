def insertionSort(aList):
    for i in range(1, len(aList)):
        curValue = aList[i]
        p = i

        while(p > 0 and curValue < aList[p-1]):
            aList[p] = aList[p-1]
            p = p-1
        aList[p] = curValue

def selectionSort(aList):
    for i in range(len(aList)):
        minIndex = i
        for j in range(i+1, len(aList)):
            if aList[j] < aList[minIndex]:
                minIndex = j
        if minIndex != i:
            temp = aList[i]
            aList[i] = aList[minIndex]
            aList[minIndex] = temp

# O(n2), stable and adaptive.
# O(n) when the array is almost sorted. Don't chek the array is already sorted on every step.
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

