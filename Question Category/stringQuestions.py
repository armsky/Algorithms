from heapAndStack import *

"""
1. Reverse a string
"""
def reverse(s):
    r = list()
    for i in xrange(len(s)-1, -1, -1):
        r.append(s[i])
    return ''.join(r)

def reverse2(s):
    r = list()
    for i in reversed(xrange(len(s))):
        r.append(s[i])
    return ''.join(r)

"""
2. check if it is a palindrome
"""
def isPalindrome(s):
    if s:
        r = list()
        for char in s:
            if char.isalnum():
                r.append(char.lower())
        for i in xrange(0, len(r)/2):
            if r[i] != r[-(i+1)]:
                return False
        return True
    else:
        return True

"""
3. Check if the braces are in pairs
"""
# Use Stack
def isPairedBraces(s):
    if len(s) >= 1:
        stack = Stack()
        pushChars = "([{"
        popChars = ")]}"
        for char in s:
            if char in pushChars:
                stack.push(char)
            elif char in popChars:
                if stack.isEmpty():
                    return False
                else:
                    popedChar = stack.pop()
                    if popedChar != pushChars[popChars.index(char)]:
                        return False
            else:
                return False
        return True
    else:
        return False
# Use list
def isPaired(s):
    stack = list()
    pushChars, popChars = "([{" , ")]}"
    for char in s:
        if char in pushChars:
            stack.append(char)
        elif char in popChars:
            if len(stack) == 0:
                return False
            else:
                if stack.pop() != pushChars[popChars.index(char)]:
                    return False
        else:
            return False
    return True

"""
3. Test if string a pangram
    Pangram are words or sentences containing every letter of the alphabet at least once.
"""
def isPangram(s):
    # Create a full set with list (string) of all chars
    f = set('abcdefghijklmnopqrstuvwxyz')
    if f - set(s.lower()) is None:
        return "pangram"
    else:
        return "not pangram"

"""
4. Find next bigger permutation
"""
# Bigger is Greater, next bigger permutation (hacker rank)
def bigger(s):
    # Find the first index that can be swap
    i = len(s) - 2
    while i >= 0 and s[i] >= s[i+1]:
        i -= 1
    if i < 0:
        print "no answer"
    else:
        # Swap this char with s[-1] (smallest)
        ns = list(s)
        ns[i], ns[-1] = ns[-1], ns[i]
        # After index i, find the lowest permutation
        first_part = ns[:i+1]
        second_part = sorted(ns[i+1:])
        r = first_part + second_part
        print ''.join(r)
"""
# Given a list of distinct integers, count the number of ordered pairs
# of integers in the list such that the first is larger than the second.
"""
"""
5. Longest Palindromic Substring
"""
# Maintain a boolean table, table[i][j] is true is a[i..j] is palindromes
# O(n^2)
def longestpalindromic(a):
    n = len(a)
    table = [[0 for y in xrange(n)] for x in xrange(n)]
    maxLength = 1
    # All substrings of length 1 are true
    for i in xrange(n):
        table[i][i] = 1
    # Check for substring of length 2
    for i in xrange(n-1):
        if a[i] == a[i+1]:
            table[i][i+1] = 1
            start = i
            maxLength = 2
    # check substring greater than 2
    for k in xrange(3, n+1): # k is length of substring
        for i in xrange(n-k+1): # i is starting index
            j = i + k - 1 # j is ending index

            if table[i+1][j-1] != 0 and a[i] == a[j]:
                table[i][j] = 1
                if k > maxLength:
                    start = i
                    maxLength = k
    return a[start : start + k]



