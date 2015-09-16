"""
merge two list
"""
def mergelist(a, b):
    c = Node(None)
    head = c
    while a and b:
        if a.val <= b.val:
            node = Node(a.val)
            a = a.next
        else:
            node = Node(b.val)
            b = b.next
        c.next = node
        c = c.next

    while a:
        node = Node(a.val)
        c.next = node
        c = c.next
        a = a.next

    while b:
        node = Node(b.val)
        c.next = node
        c = c.next
        b = b.next
    if c:
        return head.next
    else:
        return None
"""
Given a list of numbers in increasing order find the first missing number
 Ex: 1 2 3 4 5 6 8 9 11 return 7
     1 2 3 4 5 7 8 9 11 return 10
"""
def findmissing(a):
    if not a:
        return None
    r = len(a)-1
    l = 0
    while r > l:
        m = (l + r) /2
        if a[m] - a[l] > m - l:
            r = m - 1
        else:
            if l == m:
                break
            l = m + 1
    if l != r and a[l] + 1 != a[r]:
        return None
    return a[l]+1
