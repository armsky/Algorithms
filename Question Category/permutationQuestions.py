"""
1.Generates the next permutation lexicographically after a given permutation.
"""
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
2. Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

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

"""
3. The set [1,2,3,...,n] contains a total of n! unique permutations.

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

class Solution:
    # @return a string
    def getPermutation(self, n, k):
        nums = []
        # There would be n! permutations total.
        factorial = [1] * (n+1)
        nums = range(1, n+1) # Create a list [1, n+1]
        for i in xrange(1, n+1):
            factorial[i] = factorial[i-1] * i

        result = ""
        k -= 1
        for i in xrange(n, 0, -1):
            j = k / factorial[i-1]
            k = k % factorial[i-1]
            result += str(nums.pop(j))

        return result

"""
4. Letter combinations of Phone numbers
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
"""
def letterCombinations(self, digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    if not digits:
        return []

    def generate(deep, temp, result, digits, board):
        if deep == len(digits):
            result.append(temp)
            return
        digit = digits[deep]
        for char in board[digit]:
            generate(deep+1, temp+char, result, digits, board)

    result = []
    temp = ""
    deep = 0
    board = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
        }
    generate(0, temp, result, digits, board)
    return result

"""
5. Generate parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
"""
# Initial solution, will have TLE
def generateParenthesis(self, n):
    def insert(n, temp, re):
        if n == 0:
            if temp not in re:
                re.append(temp)
            return
        insert(n-1, "()"+temp, re)
        insert(n-1, temp+"()", re)
        for i in xrange(len(temp)):
            if temp[i] == "(":
                insert(n-1, temp[0:i+1]+"()"+temp[i+1:], re)
        return

    re = []
    if n >= 1:
        insert(n-1, "()", re)
        return re
    else:
        return [""]

# A better solution
def generateParenthesis(self, n):
    def insert(temp, left, right, re):
        # Handle ")("
        if left > right:
            return
        if left == 0 and right == 0:
            re.append(temp)
            return re
        if left > 0:
            insert(temp+"(", left-1, right, re)
        if right > 0:
            insert(temp+")", left, right-1, re)


    re = []
    if n >= 1:
        insert("", n, n, re)
        return re
    else:
        return [""]


