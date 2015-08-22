"""
1. Find pead element.
A peak element is an element that is greater than its neighbors.
Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.
The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
You may imagine that num[-1] = num[n] = -∞.
For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
Note:
    Your solution should be in logarithmic complexity.
"""
class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        r = len(nums) - 1
        l = 0
        while r > l:
            m = (r+l)/2
            if nums[m] > nums[m+1]:
                r = m
            else:
                l = m+1
        return l

"""
2. 3 Sum closest
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
def threeSumClosest(self, nums, target):
    if len(nums) < 3:
        return None
    diff = nums[0]+ nums[1]+ nums[2] - target
    nums.sort()
    # Be careful for the bound here, must make sure the subarray has at least 2 elements
    for i in xrange(len(nums)-2):
        tft = target - nums[i]
        temp = self.twoSum(nums[i+1:], tft)
        if abs(temp) < abs(diff):
            diff = temp
    return diff + target

def twoSum(self, a, target):
    l = 0
    r = len(a) -1
    mindiff = a[l] + a[l + 1] - target
    while r > l:
        if a[l] + a[r] == target:
            return 0
        if abs(a[l]+a[r]-target) < abs(mindiff):
            mindiff = a[l]+a[r]-target
        if a[l] + a[r] > target:
            r -= 1
        else:
            l += 1
    return mindiff
"""
3. 3 Sum.
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
"""

# NOTE:
# 1. Sort the list A
# 2. Pick A[i], and find target of -A[i], becomes a problem of 2 Sum
#       Only need to scan A[i+1:] each time
# 3. Be careful about the duplicate value
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        nums.sort()
        result = []
        for i in xrange(len(nums)):
            target = 0 - nums[i]
            temp = self.twosum(nums[i+1:], target)
            if temp:
                for one in temp:
                    if one not in result:
                         result.append(one)
        return result

    # This may have more than one pair of result
    def twosum(self, a, target):
        table = {}
        re = []
        for num in a:
            if target - num not in table:
                table[num] = 1
            else:
                re.append([0-target, target-num, num])
        if re:
            return re
        else:
            return None
"""
4.
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.
"""
# A real good solution
# If i is solution for station[0..n], there must not exist a k that sum[k:i-1] > 0
# otherwist the solution should be k. so sum[k:i-1] < 0
# Which also means, sum[i:n] must > 0
# Then the problem becomes: find the last k make sum[k:i-1] < 0, so [i:n] is the longest subarray
# that fullfill sum[i:n] > 0
# O(n) time, boom!
def canCompleteCircuit(self, gas, cost):
    sum = 0
    total = 0
    for i in xrange(len(gas)):
        sum += (gas[i] - cost[i])
        total += (gas[i] - cost[i])
        if sum < 0:
            k = i
            sum = 0
    if total < 0:
        return -1
    else:
        return k + 1
"""
5. Sort colors.
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?
"""
class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.

    # One pass solution
    def sortColors(self, nums):
        redst = 0
        bluest = len(nums) - 1
        i = 0
        while i < bluest + 1:
            if nums[i] == 0:
                nums[i], nums[redst] = nums[redst], nums[i]
                i += 1
                redst += 1
                continue
            if nums[i] == 2:
                nums[i], nums[bluest] = nums[bluest], nums[i]
                # Do not increase i here
                bluest -= 1
                continue
            i += 1
        return

    # counting sort solution
    def sortColors2(self, nums):
        from collections import defaultdict
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        start = 0
        for i in xrange(3):
            nums[start:count[i]+start] = [i] * count[i]
            start += count[i]
            print nums
        print nums
"""
6. Given an array of size n, find the majority element. The majority element is the element that appears more than [n/2] times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""
# Moore's voting algorithm
# O(n) time, O(1) space
def majorityElement(self, nums):
    candidate = None
    count = 1
    for num in nums:
        if num == candidate:
            count += 1
        else:
            count -= 1
        if count == 0:
            candidate = num
            count = 1
    return candidate

"""
7. Given an integer array of size n, find all elements that appear more than [n/3] times. The algorithm should run in linear time and in O(1) space.
"""
# Only Moore could be possible
# Since there could exist at most two majority numbers, keep track of them two
def majorityElement2(self, nums):
    count1 = count2 = 0
    can1, can2 = None, None
    for num in nums:
        if num == can1:
            count1 += 1
        elif num == can2:
            count2 += 1
        elif count1 == 0:
            can1 = num
            count1 = 1
        elif count2 == 0:
            can2 = num
            count2 =1
        else:
            count1 -= 1
            count2 -= 1
        print (can1, can2), count1, count2
    size = len(nums)
    return [n for n in (can1, can2) if n is not None and nums.count(n) > size/3]
"""
Given a sorted array of integers, find the starting and ending position of a given target value.
Your algorithm's must beO(log n). If not found, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""
    # Two Binary search to find the left bound and right bound
    # Be careful with corner cases (they are a lot...)
    def searchRange(self, nums, target):
        res = [-1,-1]
        if not nums:
            return res
        ll = 0
        lr = len(nums) -1
        while ll <= lr:
            m = (ll + lr) / 2
            if nums[m] < target:
                ll = m+1
            else:
                lr = m-1
        rl = ll
        rr = len(nums) -1
        while rl <= rr:
            m = (rl + rr) / 2
            if nums[m] <= target:
                rl = m+1
            else:
                rr = m-1
        if ll <= rr:
            return [ll, rr]
        return res
