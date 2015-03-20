def quicksort(ar, l, r):
    count = 0
    subtotal1 = 0
    subtotal2 = 0
    pivot = ar[r]
    i = l
    for j in xrange(l, r):
        if ar[j] < pivot:
            ar[j], ar[i] = ar[i], ar[j]
            i +=1
            count += 1
    ar[r], ar[i] = ar[i], ar[r]
    count += 1
    if l < i-1:
        subtotal1 = quicksort(ar, l, i-1)
    if i+1 < r:
        subtotal2 = quicksort(ar, i+1, r)
    return count+subtotal1+subtotal2


def insertsort(ar, n):
    if n > 1:
        count = 0
        for i in xrange(1, n):
            p = i
            cur = ar[i]
            while p > 0 and ar[p-1] > cur:
                ar[p] = ar[p-1]
                p -= 1
                count += 1
            ar[p] = cur
        return count
    else:
        return 0

n = int(input())
ar = [int(x) for x in raw_input().strip().split()]
# CANNOT just use: ar1 = ar !!! Must make a new list
ar1 = list(ar)
count1 = quicksort(ar, 0, n-1)
count2 = insertsort(ar1, n)
print count2-count1
