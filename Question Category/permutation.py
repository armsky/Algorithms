# Generates the next permutation lexicographically after a given permutation.
# It changes the given permutation in-place.
def nextPermutation(s):
    # s is a array(list in python)
    """
    Find the highest index i such that s[i] < s[i+1].
    If no such index exists, the permutation is the last permutation.
    """
    for i in reversed(xrange(len(s))):
        if s[i] > s[i-1]:
            break
    else:
        return []
    i -= 1
    """
    Find the highest index j > i such that s[j] > s[i].
    Such a j must exist, since at least i+1 is such an index.
    """
    for j in reversed(xrange(i+1, len(s))):
        if s[j] > s[i]:
            break
    """
    swap s[i] with s[j]
    """
    s[i], s[j] = s[j], s[i]
    """
    Reverse all the order of all of the elements after index i
    """
    s[i+1 :] = reversed(s[i+1 : ])
    # s[i+1:].sort()
    return s

"""
2. The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
"""

def getPermutation(self, n, k):
    nums = []
    factorial = [1] * (n+1)
    for i in xrange(1, n+1):
        nums.append(str(i))
        factorial[i] = factorial[i-1] * i

    result = ""
    k -= 1
    for i in xrange(n, 0, -1):
        j = k / factorial[i-1]
        k = k % factorial[i-1]
        result += nums[j]
        del nums[j]

    return result
"""
3. Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        result = []
        stack = []
        level = 1
        self.get_combination(n, k, level, stack, result)
        return result

    def get_combination(self, n, k, level, stack, result):
        if len(stack) == k:
            # Must make a copy of stack and append it to result
            result.append(list(stack))
            return
        for i in xrange(level, n+1):
            stack.append(i)
            self.get_combination(n, k, i+1, stack, result)
            stack.pop()

