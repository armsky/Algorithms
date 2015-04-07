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

# b. DP implementation, O(n^2)
def lis(arr):
    n = len(arr)
    result = [1]*n # Initialize LIS values
    # Compute optimized LIS in Bottom Up manner
    for i in xrange(1, n):
        for j in xrange(0, i):
            if arr[i] > arr[j] and result[i] < result[j] +1:
                result[i] = result[j] +1
    # Pick the maximum of lis
    return max(result)

# c. A O(n log n) approach:
# Replace the second for loop, do a binary search, use c[] as:
# smallest end-element of an i-length increasing subsequence of original sequence
# C[] should remain sorted, find a c[j]<=arr[i]<=c[j+1]
def lis(arr):
    n = len(arr)
    c = [arr[0]]
    sz = 1
    for i in xrange(n):
        # Case 1: update the smallest value of arr
        if arr[i] < c[0]:
            c[0] = arr[i]
        # Case 2: append the largest element so far to c[]
        elif arr[i] > c[sz-1]:
            c[sz] = arr[i]
            sz += 1
        # Case 3: suppose there is a subsequence ending in arr[i]
        # Find the place in c[] and update it
        else:
            c[cell_index(c, 0, sz-1, arr[i])] = arr[i]
    return len(c)

def cell_index(c, left, right, val):
    # Binary search to find the index of arr[i] should put into c[]
    while right - left > 1:
        m = (left + right)/2
        if c[m] >= val:
            right = m
        else:
            left = m
    return right

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
   reverse(a, 0, n-1)

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

# III. Store adjacent diff into another array, then find the maximum sum subarray
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

"""
5. randomizing an array (shuffle algorithm)
"""
# Fisher-Yates: start from the last element, swap it with randomly selected front one.
# O(n) time
import random
def shuffle(arr):
    n = len(arr)

    for i in xrange(n-1, 0, -1)
        # Random generate an index [0, i]
        j = random.randrange(0, i+1)  #randrange will do [a, b)
        arr[i], arr[j] = arr[j], arr[i]

"""
6. Given a array of int, find two numbers with sum as a given x
"""
# I. Naive: O(n^2), two loops
# II. Sort the array first, use two pointer, only one Loop O(n)
#   Depending one the sorting algorithm, Usually O(n log n)
def find(a, x):
    a = sorted(a)
    l = 0
    r = len(a) - 1
    while r > l:
        if a[l] + a[r] == x:
            return
        elif: a[l] + a[r] < x:
            l += 1
        else:
            r -= 1
    return None
# III. Use Hash Map, only works if range of numbers is KNOWN
# O(n) time, O(R) space, R is range of numbers
def find(a, x):
    d = dict()
    for num in a:
        if d.has_key[x-num]:
            return
        else:
            d.[num] = 1


"""
7. Josephus Problem
    An array of n, every k steps, execute one element, find the only
    safe positon. O(n) time
"""
def josephus(n, k):
    if n == 1:
        return 1
    # The position returned by josephus(n-1, k) is adjusted
    # because it considers the original position k%n + 1 as 1
    return (josephus(n-1, k) + k-1) % n +1;
