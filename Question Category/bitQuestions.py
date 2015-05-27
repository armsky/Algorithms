"""
NOTE:
1. OR: is used to setting a bit.( | 1 )
2. AND: is used to clearing a bit ( & 0 )
3. XOR: for flipping bit ( ^ 1 ) x^1 = ~x
Usages:
N << k = N*(pow(2,k))
N >> k = floor(N/pow(2,k))
N & 7	= last 3 bits in N, N & (pow(2, k)-1) = last k bits in N
~N + 1 = -N
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
