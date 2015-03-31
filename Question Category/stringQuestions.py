from heapAndStack import *

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

# Test if string a pangram
def isPangram(s):
    # Create a full set with list (string) of all chars
    f = set('abcdefghijklmnopqrstuvwxyz')
    if not f - set(s.lower()):
        return "pangram"
    else:
        return "not pangram"


# Bigger is Greater, next bigger permuttion (hacker rank)
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

