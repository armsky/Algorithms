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
sellany number of shares or not make any transaction. What is the maximum
profit you can get.
"""
#NOTE: Stock trade is easy if time goes backwards!
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
7. Pots of godd game
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

