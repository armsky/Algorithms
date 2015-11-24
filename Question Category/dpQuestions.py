"""
Dynamic Programming is an algorithmic paradigm that solves a given
complex problem by breaking it into subproblems and stores the results
of subproblems to avoid computing the same results again.
If a problem can be solved using DP, usually has such two main properties:
    1. Overlapping Subproblems (BST is not a DP problem since it don't has common problems)
    2. Optimal Substructure
"""
"""
I. For overlapping problem, we have:
    a. Memoization (Top Down): Initialize a lookup table with nil values, whenevert we need
        solution to a subproblem, we first look into the lookup table before calculate, it
        the value not there, we calculate and put the result into table
    b. Tabulation (Bottom Up): build a table by filling entries one by one
II.For Optimal Substructure: a optimal solution of the given problem can be obtained
   by using optimal solutions of its subproblems.
   A shortest path problem can use this way, but longest path cannot
"""

"""
1. Find Maximum subarray:
Given an array of n elements, find the maximum possible sum of a :
    1. contiguous subarray
    2. not necessarily contiguous subarray
"""
def max_sub_con(a):
    n = len(a)
    result = list(a) # make a copy of a
    for i in xrange(1, n):
        if a[i] + result[i-1] >= 0:
            result[i] = result[i-1] + a[i]
    return max(result)

def max_sub_non_con(a):
    result = 0
    all_negative = True
    for x in a:
        if x > 0:
            result += x
            all_negative = False
    if all_negarive:
        return max(a)
    else:
        return result

"""
2. Stock Maximize
Given an array of stock share price, each day, you can either buy one share,
sell any number of shares or not make any transaction. What is the maximum
profit you can get.
"""
# NOTE: Stock trade is easy if time goes backwards!
# Find highest price backwards in time
def max_profit(a):
    profit = 0
    m = 0
    buy = [1] * len(a) # 1 for buy, 0 for sell
    for i in xrange(len(a)-1, -1, -1):
        if m <= a[i]:
            m = a[i]
            buy[i] = 0
        profit += m-a[i]
    return profit
# More stock questions from LeetCode:
# a. If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock
def maxProfit(self, prices):
        if prices:
            min = prices[0]
            max = 0
            for i in xrange(1, len(prices)):
                price = prices[i]
                if price < min:
                    min = price
                if price - min > max:
                    max = price - min
            return max
        else:
            return 0
# b. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# The problem becomes to find each ascending sub-array, buy stock at the first
# day of sub-array, sell the stock at the end of the sub-array. since the total
# delta equals the sum of difference of each adjacent element:
def maxProfit(self, prices):
    delta = 0
    if not prices:
        return 0
    for i in xrange(1, len(prices)):
        if prices[i] > prices[i-1]:
            delta += prices[i] - prices[i-1]

    return delta
# c. You may complete at most two transactions.
def maxProfit(self, prices):
    if not prices:
        return 0
    p = prices
    n = len(p)
    # Use two arrays, left[i] means until ith element the max profit
    # right[i] means the max profit from ith to the array end
    left = [0]
    right = [0]*n

    min_p = p[0]
    for i in xrange(1, n):
        left.append(max(p[i] - min_p, left[i-1]))
        min_p = min(p[i], min_p)

    max_p = p[-1]
    for i in xrange(n-2, -1, -1):
        right[i] = max(max_p - p[i], right[i+1])
        max_p = max(p[i], max_p)

    max_profit = 0
    for i in xrange(n):
        max_profit = max(left[i] + right[i], max_profit)
    return max_profit
# d. You may complete at most k transactions.
# Use two array global[i][j] and local[i][j]
# Global means in ith day, make j transactions the best profit
# Local means ... and sell all in jth transaction, the profit (not best)
# O(k*n) time, O(k) space
def maxProfit(self, k, prices):
    p = prices
    if not p:
        return 0
    if k > len(p):
        # Use scenario II
        return
    g = [0] * (k+1)
    l = [0] * (k+1)
    for i in xrange(len(p)-1):
        diff = p[i+1] - p[i]
        for j in xrange(k, 0, -1):
            l[j] = max(g[j-1] + max(diff, 0), l[j] + diff)
            g[j] = max(g[j], l[j])
    return g[k]

"""
3. Longest Increasing Subsequence
"""
def lis(a):
    def switch(left, right, num, r):
       while right - left > 1:
        mid = (left+right)/2
        if r[mid] >= num: #NOTE: careful with the >= here
            right = mid
        else:
            left = mid
    r[right] = num
    return

    r = []
    r.append(a[0])
    sz = 1
    for i in xrange(1, len(a)):
        if a[i] <= r[i]:
            r[0] = a[i]
        elif a[i] > r[-1]:
            r.append(a[i])
            sz += 1
        else:
            switch(0, sz-1, a[i], r)
    return sz

"""
4. Candies
All the children sit in a line, and each  of them has a rating score according to his or her performance in the class.  Alice wants to give at least 1 candy to each child. If two children sit next to each other, then the one with the higher rating must get more candies. Alice wants to save money, so she needs to minimize the total number of candies.
"""
# Two loops, one forward and the other backword.
def candies(a):
    n = len(a)
    c = [1] * n
    for i in xrange(1, n):
        if a[i] > a[i-1]:
            c[i] = c[i-1]+1
    for i in xrange(n-2, -1, -1):
        if a[i] > a[i+1]:
            c[i] = max(c[i], c[i+1]+1)
    return sum(c)

"""
5. Knapsack: Find expected sum in a list of integers
return the sum (k) of numbers as near as possible, but not exceeding
is no element is selected, then sum is 0
"""
# a. if each element of list can be selected multiple times
# Time: O(NK)
def knapsack(a, k):
    n = len(a)
    # Build a temp to store possible expected sum of 0..k
    dp = [0] * (k+1)
    a.sort()
    for g in xrange(1, k+1): # k slots in knapsack
        for i in xrange(n): # each candidate in a
            if a[i] <= g:
                dp[g] = max(dp[g], a[i] + dp[g - a[i]])
    return dp[k]

# b. if each element of list can be selected only once
# simple case
def knapsack2(a,k):
    a.sort()
    temp = 0
    for i in xrange(n):
        if a[i] + temp <= k:
            temp += a[i]
    return temp


"""
6. Knapsack(0/1): a list of items with weight and value
Put items into sack, not exceed the total weigt limit, make value maxium.
"""
# a. DP solution, Time: O(NW)
def Knapsack(a, W):
    # a value table
    table = [[0 for w in xrange(W+1)] for j in xrange(len(a))]
    for j in xrange(1, len(a)+1):
        wt = a[j].wt
        val = a[j].val
        for w in xrange(1, W+1):
            if wt > W:
                table[j][w] = table[j-1][w]
            else:
                table[j][w] = max(table[j-1][w], val + table[j-1][w - wt])
    result = []
    w = W
    for i in xrange(len(a), 0, -1):
        if table[i][w] != table[i-1][w]:
            result.append(a[i-1])
            w -= a[i-1].wt
    return result

"""
If not (0/1): can choose items multiple times
"""
# 1. Optimize a, if wt[i] < wt[j] and val[i] > val[j], delete j.

# 2.

"""
7. Pots of gold game
A list of pots with gold coins, you can pick the first pot or the last one.
If you starts the game, opponent can also play optimal, how do you win
"""
pots = [...]
def optimal(left, right):
    if left > right:
        return 0
    a = pots[left] + min(optimal(left+2, right),
                        optimal(left+1, right-1))
    b = pots[right] + min(optimal(left, right-2,
                        optimal(left+1, right-1))
    return max(a,b)


"""
8. Longest Palindromic Substring
"""
# Maintain a boolean table, table[i][j] is true is a[i..j] is palindromes
# O(n^2)
def longestpalindromic(a):
    n = len(a)
    table = [[0 for y in xrange(n)] for x in xrange(n)]
    maxLength = 1
    # All substrings of length 1 are true
    for i in xrange(n):
        table[i][i] = 1
    # Check for substring of length 2
    for i in xrange(n-1):
        if a[i] == a[i+1]:
            table[i][i+1] = 1
            start = i
            maxLength = 2
    # check substring greater than 2
    for k in xrange(3, n+1): # k is length of substring
        for i in xrange(n-k+1): # i is starting index
            j = i + k - 1 # j is ending index

            if table[i+1][j-1] != 0 and a[i] == a[j]:
                table[i][j] = 1
                if k > maxLength:
                    start = i
                    maxLength = k
    return a[start : start + k]
"""
9. Given a string s and a dictionary of words dict, determine if s can be segmented into
a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
"""
def wordBreak(self, s, wordDict):
    if not wordDict or not s:
        return False
    dp = [False] * (len(s) +1)
    dp[0] = True

    for i in xrange(1, len(s)+1):
        for k in xrange(i):
            if dp[k] and s[k:i] in wordDict:
                dp[i] = True
    return dp[len(s)]

"""
10. Jump game I.
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""
# Notice that in index i, the range that could jump to is [i:i + nums[i]]
def canJump(self, nums):
    maxindex = 0
    for i in xrange(len(nums)):
        if i > maxindex:
            return False
        elif maxindex >= len(nums) - 1:
            return True
        else:
            maxindex = max(maxindex, i + nums[i])

"""
11. Jump game II.
reach the last index in the minimum number of jumps.

For example: A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
"""
# NOTE instead of tracking the length it can jump, track the times of jump that will
# reach to the last index
def jump(self, nums):
    cur_length = 0
    njump = 0
    i = 0
    while cur_length < len(nums) -1:
        last_length = cur_length
        for i in xrange(i, last_length+1):
            cur_length = max(cur_length, i + nums[i])
        njump += 1
        if cur_length == last_length:
            return -1
    return njump

"""
12. Palindrome Partitioning
Given a string s, cut s into some substrings such that every substring is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of s.

Example
For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""
# O(n^2) time, O(n) space
# Credit to: https://leetcode.com/discuss/53981/56-ms-python-with-explanation
def minCut(self, s):
    # acceleration
    if s == s[::-1]: return 0
    for i in range(1, len(s)):
        if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
            return 1
    # algorithm
    cut = [x for x in range(-1,len(s))]  # cut numbers in worst case (no palindrome)
    for i in range(len(s)):
        r1, r2 = 0, 0
        # use i as origin, and gradually enlarge radius if a palindrome exists
        # odd palindrome
        while i-r1 >= 0 and i+r1 < len(s) and s[i-r1] == s[i+r1]:
            cut[i+r1+1] = min(cut[i+r1+1], cut[i-r1]+1)
            r1 += 1
        # even palindrome
        while i-r2 >= 0 and i+r2+1 < len(s) and s[i-r2] == s[i+r2+1]:
            cut[i+r2+2] = min(cut[i+r2+2], cut[i-r2]+1)
            r2 += 1
    return cut[-1]

"""
13. Longest common subsequence(LCS).
Your code should return the length of LCS.

For "ABCD" and "EDCA", the LCS is "A" (or "D", "C"), return 1.
For "ABCD" and "EACB", the LCS is "AC", return 2.
"""
def longestCommonSubsequence(self, A, B):
    if not A or not B:
        return 0
    m = len(A)
    n = len(B)
    # dp[i][j] means until A[i] and B[j] the LCS is
    dp = [[0 for x in range(n+1)] for y in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

"""
14. Longest common substring.

Return the length of it.

Example
Given A = "ABCD", B = "CBCE", return 2.

Note
The characters in substring should occur continuously in original string. This is different with subsequence.
"""
def longestCommonSubstring(self, A, B):
    if not A or not B:
        return 0
    m = len(A)
    n = len(B)
    dp = [[0 for x in range(n+1)] for y in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
    return max(map(max, dp))
