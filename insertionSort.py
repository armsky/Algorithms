def insertionSort(aList):
    for i in range(1, len(aList)):
        curValue = aList[i]
        p = i

        while(p > 0 and curValue < aList[p-1]):
            aList[p] = aList[p-1]
            p = p-1
        aList[p] = curValue

aList = [21, 2, 45, 103, 0, 64]
insertionSort(aList)
print aList


