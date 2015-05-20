"""
1. McDonald's sell chicken Nuggets in packages of 6, 9 or 20.
Given a number n, find non-negetive integer values of a,b and c that:
    6a + 9b + 20c = n
"""
def mc(n):
    return n >= 0 and (n == 0 or mc(n-6) or mc(n-9) or mc(n-20))
