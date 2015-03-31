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
2. Longest increasing subsequence
"""


"""
3. Rotate array by n elements.
"""

"""
4. Find max difference in an unsorted array. The index of min < index of max
    Can't sort the array. similiar: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""
