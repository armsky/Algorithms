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
def knaosack(a, k):
    n = len(a)
    # Build a temp to store possible expected sum of 0..k
    dp = [0] * (k+1)
    a.sort()
    for g in xrange(1, k+1): # k slots in knapsack
        for i in xrange(0, n): # each candidate in a
            if a[i] <= g:
                dp[i] = max(dp[i], a[i] + dp[g - a[i]])
    return dp[k]

# b. if each element of list can be selected only once



