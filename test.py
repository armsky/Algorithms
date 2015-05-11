def maxProfit( prices):
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
        print left
        max_p = p[-1]
        for i in xrange(n-2, -1, -1):
            right[i] = max(max_p - p[i], right[i+1])
            max_p = max(p[i], max_p)
        print right
        max_profit = 0
        for i in xrange(n):
            max_profit = max(left[i] + right[i], max_profit)
        return max_profit
a = [6,1,3,2,4,7]
print  maxProfit(a)
