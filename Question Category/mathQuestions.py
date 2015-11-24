"""
1. Implement int sqrt(int x).

Compute and return the square root of x.
"""
def mySqrt(self, x):
    """
    :type x: int
    :rtype: int
    """
    # the root of x will not bigger than x/2 + 1
    if x == 0:
        return 0
    elif x == 1:
        return 1
    l = 0
    r = x/2 + 1
    while r >= l:
        mid = (r + l) /2
        temp = x / mid # use division here, not square
        if temp == mid:
            return mid
        elif temp < mid:
            r = mid - 1
        else:
            l = mid + 1
    return r

"""
2. Perfect Squares.
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
"""
def numSquares(self, n):
    """
    :type n: int
    :rtype: int
    """
    # Will have TLE
    import sys
    sqs = []
    dp = [sys.maxsize] * (n+1)
    dp[0] = 0
    for i in xrange(n/2 +1):
        sqs.append(i*i)
    for i in xrange(0, n+1):
        for j in xrange(len(sqs)):
            if i + sqs[j] <= n:
                dp[i+sqs[j]] = min(dp[i+sqs[j]], dp[i] + 1)
            #print dp
    return dp[n]

# Based on Lagrange's Four-Square Theorem (Number theory):
# every natural number can be represented as the sum of four integer squares.
def numSquares(self, n):
    import math
    while n % 4 == 0:
        n = n / 4
    if n % 8 == 7:
        return 4
    a = 0
    while a*a <=:
        b = int(math.sqrt(n - a*a))
        if a*a + b*b == n:
            if a!=0 and b!=0:
                return 2
            elif a==0 or b == 0:
                return 1
            else:
                return 0
        a += 1
    return 3

"""
3. Use rand5() to get rand7()
"""
# suppose rand5() will return 0~4, so rand7() returns 0~6
def rand2():
    x = rand5()
    if x == 4:
        return rand2()
    else:
        return x % 2

def rand7():
    x = 4 * rand2() + 2 * rand2() + 1 *rand2()
    if x == 7:
        return rand7()
    else:
        return x
"""
4. Create class which stores big integers (of any length) and implement addition operation.
"""
class BigInt():

    def __init__(self, num_str):
        if num_str[0] != '-':
            self.positive = True
            self.intlist = [int(d) for d in num_str]
        else:
            self.positive = False
            self.intlist = [int(d) for d in num_str[1:]]
        self.intlist.reverse() # reverse() has NO return value!!!


    def add(self, bigint):
        if self.abs_bigger(bigint):
            a = self.intlist
            b = bigint.intlist
            positive = self.positive
        else:
            a = bigint.intlist
            b = self.intlist
            positive = bigint.positive

        if self.positive != bigint.positive:
            return self.sub(a, b, positive)
        m = len(a)
        n = len(b)
        carry = 0
        for i in range(m):
            if i < n:
                carry, val = divmod(a[i]+b[i]+carry, 10)
            else:
                carry, val = divmod(a[i]+carry, 10)
            a[i] = val
        if carry > 0:
            a.append(1)
        return positive, a

    def sub(self, a, b, positive):
        m = len(a)
        n = len(b)
        carry = 0
        for i in range(m):
            if i < n:
                if a[i] + carry >= b[i]:
                    a[i] -= b[i]
                    carry = 0
                else:
                    a[i] = a[i] + 10 - b[i]
                    carry = -1
            else:
                if a[i] + carry >= 0:
                    a[i] += carry
                    carry = 0
                else:
                    a[i] = a[i] + 10 + carry
                    carry = -1
        if a[-1] == 0:
            if len(a) != 1:
                a = a[:-1]
        return positive, a

    def abs_bigger(self, bigint):
        if len(self.intlist) > len(bigint.intlist):
            return True
        elif len(self.intlist) == len(bigint.intlist):
            for i in range(len(self.intlist)):
                if self.intlist[i] > bigint.intlist[i]:
                    return True
                elif self.intlist[i] < bigint.intlist[i]:
                    return False
            return True
        else:
            return False


# test cases:
print BigInt('0').add(BigInt('0'))
print BigInt('0').add(BigInt('1'))
print BigInt('1').add(BigInt('99'))
print BigInt('100').add(BigInt('-1'))
print BigInt('1').add(BigInt('-1'))
print BigInt('-1').add(BigInt('-100'))
print BigInt('-1').add(BigInt('100000'))

