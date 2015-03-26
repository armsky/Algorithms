"""
1.1 Is the number prime.
1.2Find all the prime factors of a number
"""
# Not a efficient way
def isPrime(num):
    return all(num % i for i in xrange(2, num))
# a little more efficient
def isPrime(num):
    return all(num % i for i in xrange(2, math.sqrt(num)+1))

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
- If n is big, sort (n log n) and find (log n)
"""
