"""
NOTE:
1. OR | : is used to setting a bit.( | 1 )
2. AND & : is used to clearing a bit ( & 0 )
3. XOR ^ : for flipping bit ( ^ 1 ) x^1 = ~x
Usages:
N << k = N*(pow(2,k))
N >> k = floor(N/pow(2,k))
N & 7	= last 3 bits in N, N & (pow(2, k)-1) = last k bits in N
~N + 1 = -N , ~N = -N - 1
"""

"""
1. Get the count of 1s in a number
"""
# a. N & 1 gives the first bit
while n > 0:
    count += n & 1
    n = n >> 1
# b. N & (N-1) will turn off the first set bit （hamming weight)
while n > 0:
    n = n & (n-1)
    count += 1
# Can be used to check if the num is a power of 2:
if n & (n-1) == 0:
    return True
# Check if this num is a power of 4:
#   Must be power of 2, the number of 0s must be even
#   The num of 0s = total bits - num of 1s

"""
2. Swap two numbers using bitwise operations
"""
a = a ^ b
b = a ^ b
a = a ^ b

"""
3. Convert decimal to binary
"""

"""
4. Flip 32 bits unsigned integers
"""
num = int(num_string)
num = num ^ 0xffffffff

"""
5. AND product.
Given two integers a and b, compute the bitwise AND amongst all natual numbers
lying between a and b, both inclusive. (0 <= a <= b <= 2^32)
"""
def and_product(a, b):
    counter = 0
    while a != b:
        a = a >> 1
        b = b >> 1
        counter += 1
    print a << counter

"""
6. Given a array, XOR all subarrays of it.
Note: if the array have even number of elements, it must be 0
If it has odd elements, only need to XOR it's odd index elements.
"""
if n %2 == 0:
        print 0
else:
    result = 0
    for j in xrange(n):
        if (j+1) % 2 == 1:
            result = result ^ nums[j]
    print result

"""
7. Reverse bits in an integer
"""
# Say this integer has M bits
def reverse_bits(n, M):
    N = 1 << M
    r = n # will store the bit-revevrsed pattern
    for i in xrange(M):
        n >> 1
        r << 1
        r |= n&1 # Give LSB of n to r
    r &= N-1 # N-1 is a mask, will clear all bits more significant than N-1
    return r

# A improved version
def reverse(n, M):
    N = 1 << M
    count = M -1
    r = n

    while n != 0:
        n >> 1
        r << 1
        r |= n&1
        count -= 1
    r << count
    r &= N-1
    return r

"""
8. Bitwise AND of Numbers Range
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.
NOTE: Only need to see the common left bits (left header)
"""
def rangeBitwiseAnd(self, m, n):
    p = 0
    while m != n:
        m >>= 1
        n >>= 1
        p += 1
    return m << p
