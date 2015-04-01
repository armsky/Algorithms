"""
1. Maximum subarray problem. Give an array, find the contiguous subarray that has the
    largest sum. (The array must have at least 1 positive number)
"""
# I. Kadane's Algorithm. A DP resolution
# O(n) time
def maxSub(a):
    n = len(a)
    max_so_far = 0
    max_ending_here = 0
    for i in xrange(n):
        max_ending_here = max_ending_here + a[i]
        if max_ending_here <= 0:
            max_ending_here = 0
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
    return max_so_far

"""
2. Longest increasing subsequence (LIS)
# unlike substrings, subsequences are not required to occupy
consecutive positions within the original sequences.
"""
# a. Naive recursive implementation:
#   Length of LIS ending with arr[n-1] use max_ending_here
#   Overall maximum as the LIS may end before arr[n-1] use max_ref
def lis(arr):
    result = 1
    n = len(arr)
    _lis(arr, n, result) #_lis() stores its result
    return result

def _lis(arr, n, max_ref):
    if n == 1:
        return 1
    max_ending_here = 1
    # Recursively get all LIS ending with arr[0], arr[1], ..., arr[n-2]
    for i in xrange(1, n):
        res = _lis(arr, i, max_ref)
        if arr[i-1] < arr[n-1] and res+1 > max_ending_here:
            max_ending_here = res + 1
    if max_ref < max_ending_here:
        max_ref = max_ending_here
    return max_ending_here

# DP implementation
def lis(arr):
    n = len(arr)
    lis = [1]*n # Initialize LIS values
    # Compute optimized LIS in Bottom Up manner
    for i in xrange(1, n):
        for j in xrange(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] +1:
                lis[i] = lis[j] +1
    # Pick the maximum of lis
    return max(lis)

# A O(n log n) approach:
def lis(arr):
    n = len(arr)
    length = 1 # alway points to next empty slot, this is also the result
    tailtable = []
    tailtable.append(arr[0])
    for i in xrange(1, n):
        # case 1: if arr[i] is the smallest, starts new list of length 1
        if arr[i] < tailtable[0]:
            tailtable[0] = arr[i]
        # case 2: if arr[i] is the largest
        elif arr[i] > tailtable[length-1]:
            tailtable.append(arr[i])
            length += 1
        else:



"""
3. Rotate array by d elements.
"""
# I. Use temp array, O(n) time, O(d) space
def rotate(a, d):
    temp = a[0:d]
    a = a[d:]
    a = a + temp

# II. Reversal Algorithm
# Let AB are two parts of a, reverse A as Ar, reverse B as Br
# Reverse ArBr as BA. O(n) time, O(1) space
def reverse(a, l, r):
    while l < r:
        a[l], a[r] = a[r], a[l]
        l += 1
        r -= 1

def rotate(a, d):
   reverse(a, 0, d-1)
   reverse(a, d, n-1)
   reverse(d. 0, n-1)

"""
4. Find max difference in an unsorted array. The index of min < index of max
    Can't sort the array. similiar: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""
# I. Naive, use two loops, store the max diff
# O(n^2) time, O(1) space

# II. Track max_diff and the minimum number so far
# O(n) time, O(1) space
def maxDiff(a):
    max_diff = 0
    min_num = a[0]
    for i in xrange(1, len(a)):
        if a[i] - min_num > max_diff:
            max_diff = a[i] - min_num
        if a[i] < min_num:
            min_num = a[i]
    return max_diff

# III. Store adjacent diff into another array, then finf the maximum sum subarray
# O(n) time, O(n) space
def maxDiff(a):
    da = []
    for i in xrange(1, len(a)):
        da.append(a[i] - a[i-1])
    max_diff = 0
    for i in xrange(1, len(da)):
        if da[i-1] > 0:
            da[i] += da[i-1]
        if max_diff < da[i]
            max_diff < da[i]
    return max_diff
