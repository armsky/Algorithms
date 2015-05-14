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
# b. N & (N-1) will turn off the first set bit
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
1. Convert decimal to binary
"""
