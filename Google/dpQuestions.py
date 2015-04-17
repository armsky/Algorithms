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
