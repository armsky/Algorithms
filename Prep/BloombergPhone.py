# -*- coding: UTF-8 -*-
"""
1. Category words
Input : {"tea", "eat", "ate", "run","urn","cool","school"}
Output : {{"tea", "eat", "ate"},{"run","urn"}}
"""
# set and list are unhashable
def category(words):
    table = {}
    result = []
    for word in words:
        # Sort the string as list, and use string as hash key
        chars = str(sorted(list(word)))
        if chars in table:
            table[chars].append(word)
        else:
            table[chars] = [word]
    for word_list in table.values():
        if len(word_list) > 1:
            result.append(word_list)
    return result

words = ["tea", "eat", "ate", "run","urn","cool","school"]
print category(words)

"""
2. Copy a list
input:

       -----------
      |          |

A---->B--->C---->D---->E
|          ^
|          |
------------

output:

        ------------
       |            |
A'---->B'--->C'---->D'---->E''
|            ^
|            |
 ------------

 struct node
{
    node * next;
    node * jump;
    int val
}
 """
# Ask question:
# 1. Big loop? (last node.next point to another node
# 2. Duplicates values?
def copy_list(a):
    b = Node(a)
    heada = a
    headb = b
    # Copy this list without jump pointer
    while a.next:
        b.next = Node(a.next.val)
        a = a.next
        b = b.next
    a = heada
    b = headb
    while a:
        if a.jump:
            table[a.jump.val] = b
        if b.val in table:
            table[b.val].jump = b
        a = a.next
        b = b.next
    return headb


"""
3. Clone graph
Return a deep copy of graph
"""

"""
4. Continuous sequence with the largest sum
Example: input[2,-8,3,-2,4,-10] -> output: 5 (from the continuous sequence 3,-2,4).
"""
# 如果相加<0, 记作0，否则一直加下去

"""
5. shortest path to Good point.
gave a matrix, (B means cannot go through)
000
BGG
G00

calculate the shortest path between each 0 to G, so result will be

211
BGG
G11
"""
# 从G开始把周围元素加1，再从所有1开始把1周围的所有元素加1，一个队列就行了
import Queue
def shortest(ma):
    m = len(ma)
    n = len(ma[0])
    for i in range(m):
        ma[i] = list(ma[i])
    print ma
    for i in range(m):
        for j in range(n):
            if ma[i][j] == 'G':
                if valid(i-1, j, m, n, ma):
                    ma[i-1][j] = 1
                if valid(i+1, j, m, n, ma):
                    ma[i+1][j] = 1
                if valid(i, j-1, m, n, ma):
                    ma[i][j-1] = 1
                if valid(i, j+1, m, n, ma):
                    ma[i][j+1] = 1

            if ma[i][j] == '0':
                ma[i][j] = 0

    q = Queue.Queue()
    for i in range(m):
        for j in range(n):
            if ma[i][j] == 1:
                q.put((i,j))

    while q.qsize() > 1:
        i, j = q.get()
        if valid(i-1, j, m, n, ma):
            enqueue(i-1, j, i, j, ma, q)
        if valid(i+1, j, m, n, ma):
            enqueue(i+1, j, i, j, ma, q)
        if valid(i, j-1, m, n, ma):
            enqueue(i, j-1, i, j, ma, q)
        if valid(i, j+1, m, n, ma):
            enqueue(i, j+1, i, j, ma, q)
    return ma

def valid(i, j, m, n, ma):
    if 0 <= i < m and 0 <= j < n:
        if ma[i][j] != 'B' and ma[i][j] != 'G':
            return True
    return False

def enqueue(i, j, x, y, ma, q):
    if ma[i][j] == 0:
        ma[i][j] = ma[x][y]+1
        q.put((i, j))
    else:
        if ma[x][y]+1 < ma[i][j]:
            ma[i][j] = ma[x][y]+1
            q.put((i, j))

matrix = ["000",
"BGG",
"G00"
]
#print shortest(matrix)

"""
6. Sum of two linked list
7->8 + 2->2 = 1->0->0
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# reverse two linked lists, sum them up and reverse back
def list_sum(a1, b1):
    a = reverse(a1)
    b = reverse(b1)
    dummy = c = ListNode(0)
    carry = 0
    while a or b or carry:
        if a:
            carry += a.val
            a = a.next
        if b:
            carry += b.val
            b = b.next
        carry, val = divmod(carry, 10)
        c.next = ListNode(val)
        c = c.next
    return reverse(dummy.next)

def reverse(a):
    pre = None
    cur = a
    while cur:
        nex = cur.next
        cur.next = pre
        pre = cur
        cur = nex
    return pre

#a = ListNode(1)
#a.next = ListNode(2)
#a.next.next = ListNode(9)
#b = ListNode(2)
#b.next = ListNode(1)
#
#nh = list_sum(a, b)
#while nh:
#    print nh.val
#    nh = nh.next

"""
7. check parentheses is balanced
"""
# Remember if all are right parentheses
# stack will still be empty at last
stack = []
if not stack:
    return not input

"""
8. Wildcard Matching
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
"""
def isMatch(self, s, p):
    length = len(s)
    if len(p) - p.count('*') > length:
        return False
    dp = [True] + [False]*length
    for i in p:
        if i != '*':
            for n in reversed(range(length)):
                dp[n+1] = dp[n] and (i == s[n] or i == '?')
        else:
            for n in range(1, length+1):
                dp[n] = dp[n-1] or dp[n]
        dp[0] = dp[0] and i == '*'
    return dp[-1]
#dp[n] means the substring s[:n] if match the pattern i
#dp[0] means the empty string '' or s[:0] which only match the pattern '*'
#use the reversed builtin because for every dp[n+1] we use the previous 'dp'

"""
9. Longest Substring Without Repeating Characters
"""
def lengthOfLongestSubstring(self, s):
    if not s:
        return 0
    re = s[0]
    m = 1
    for i in xrange(1, len(s)):
        if s[i] not in re:
            re += s[i]
        else:
            j = re.index(s[i])
            re = re[j+1:] + s[i]
        if len(re) > m:
            m = len(re)

    return m

"""
10. Create class which stores big integers (of any length) and implement addition operation.

Store the number in array with a reversed way
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

"""
11. Print all items on k-th level of a binary tree.
Use recursive way (DFS)
"""
def klevel(root, k):
    result = []
    if not root:
        return result
    dfs(root, result, 1, k)
    return result

def dfs(node, result, cur_level, max_level):
    if not node or cur_level > max_level:
        return
    if cur_level == max_level:
        result.append(node)
        return
    dfs(node.left, result, cur_level+1, max_level)
    dfs(node.right, result, cur_level+1, max_level)

"""
12. Implement pow(x, n). X to the power of N

1.Most naive method, simply multiply x n times:
The time complecity is O(n), but will cause(stack overflow)error

2.Do division before recursive:
x^n = x^n/2 * x^n/2 * x^n%2
Time complexity is O(logN)

NOTE:
1. n might be positive or negetive
2. 0^0 = 1, 0^positive = 0, 0^negetive nonsence
"""
# @param x, a float
# @param n, a integer
# @return a float

# Recursive
def pow(self, x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / self.myPow(x, -n)
    if n % 2 == 1:
        return x * self.myPow(x, n-1)
    return self.myPow(x*x, n/2)

# Iterative
def pow2(self, x, n):
    if n == 0:
        return 1
    if n < 0:
        x = 1/x
        n = -n
    re = 1
    while n:
        if n & 1 == 1:
            re *= x
        x *= x
        n = n >> 1
    return re

