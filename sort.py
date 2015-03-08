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

aList = [21, 2, 45, 103, 0, 64, 0]
insertionSort(aList)
print aList
aList = [21, 2, 45, 103, 0, 64, 0]
selectionSort(aList)
print aList


