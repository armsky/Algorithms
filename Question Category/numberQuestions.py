"""
1.1 Is the number prime.
1.2 Find all the prime factors of a number
"""
# Not a efficient way
def isPrime(num):
    return all(num % i for i in xrange(2, num)) # all(): return True is all element in () are true
# a little more efficient
def isPrime(num):
    return all(num % i for i in xrange(2, math.sqrt(num)+1), 2)

def primeFactor(num):
    result = []
    while num%2 == 0:
        result.append(2)
        num = num/2
    for i in xrange(3, math.sqrt(num)+1, 2):
        while num % i == 0:
            result.append(i)
            num = num / i
    if num > 2:
        result.append(num)
    return result
"""
1.3: Find all prime numbers smaller than N
Much quicker than above.
"""
# Sieve of Eratosthenes algorithm
#   1. create a list of consecutive integers from 2 to n
#   2. start from p, mark 2p, 3p, 4p... they are not prime
#   3. the first number greater than p is prime, repear step 2
def sieve(n):
    result = []
    if n >= 2: # no prime smaller than 2
        arr = [0] * n # arr[i]==0 means prime, arr[i]==1 means not prime
        for i in xrange(1, n):
            if arr[i] == 0:
                result.append(i+1)
                mark_multiples(arr, i+1, n)
    return result

def mark_multiples(arr, a, n)
    # mark all multiples of 'a' but <= n as 1
    i = 2
    while i*a <= n:
        arr[i*a -1] = 1 # because index starts from 0
        i += 1

"""
2. check whether an integer is a palindrome without using arrays.
"""
def reversDigits(num):
    ori_num = num
    rev_num = 0
    while num > 0:
        rev_num = rev_num*10 + num%10
        num = num/10
    if rev_num == ori_num:
        return True
    else:
        return False

"""
3.Check if array of int contain two number that sum equal to target number
- If n is small, compare each pair, O(n^2)
- If n is big, sort (n log n) and find O(n)
"""
def find_small(a, target):
    for i in xrange(len(a)):
        for j in xrange(len(a)):
            if j != i and a[i] + a[j]:
                print a[i], a[j]

def find_big(a, target):
    a = sorted(a)
    left = 0
    right = len(a) - 1
    while left < right:
        if a[left] + a[right] == target:
            print a[left], a[right]
        elif a[left] + a[right] > target:
            right -= 1
        else:
            left += 1

"""
4. Number of trailing zeros in a number factorial.
"""
# I. Brute force, calculate and then count the zeros.
# II. Find multiple of 5, 25, 125s
def find_zeros(n):
    count = 0
    count = count + n/5 + n/25 + n/125 + ...
    return count

"""
5. Convert decimal numbers to binary and vice-versa
"""
def dec_to_bin(dec):
    i = 1
    s = 0
    while dec > 0:
        rem = dec % 2
        s = s + (i*rem)
        dec = dec/2
        i = i*10
    return s

def bin_to_dec(binn):

"""
6.  fibonacci in recursive way
"""
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        return fibonacci(n-1) + fibonacci(n-2)

"""
7. Approximate the square root of a number using binary search
"""
def sqrt(n):
    precision = 0.00001
    low = 0
    high = n
    mid = 0
    while high - low > precision:
        mid = (high+low)/2
        v = mid * mid
        if v - n > precision:
            high = mid
        else:
            low = mid
    return mid

"""
8. Given 1 byte, Check it has exactly 3 bits equals to 1
"""
# Use Kerninghan's algorithm
def has_three_set_bits(n):
    for i in xrange(3):
        if n == 0:
	    return False
	n = n & (n-1)
    return n == 0

"""
9. Given a array of numbers, find two with their sum closed to 0
"""
# Sort the array by their absolute values, and find each adjacent ones
# i.e.: 10, -50, -20, 1, 2, -5, 51, 70 => 1, 2, -5, 10, -20, -50, 51, 70
# will easily find -50 and 51

"""
10. New N Fibonacci sequence, not adding the last 2 element's but add the last n elements
EX. For n=3. Sequence =  1 1 1 3 5 9 17 ...
"""
# Observe that s[i] = 2* s[i-1] - s[i-n]
for i in xrange(n):
    s.append(1)
for i in xrange(n, target):
    s.append(2 * s[i-1] - s[i-n])

"""
11. Product of array except self.
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)
"""
#   Since result[i] = (x1 * x2 * ... * xi-1)*(xi+1 * ... * xn)
#   So we can loop the array twice, back and forth

class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        result = [1] * len(nums)
        left = 1
        for i in xrange(len(nums)-1):
            left *= nums[i]
            result[i+1] *= left
        right = 1
        for i in xrange(len(nums)-1, 0, -1):
            right *= nums[i]
            result[i-1] *= right
        return result

