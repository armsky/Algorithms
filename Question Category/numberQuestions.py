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


