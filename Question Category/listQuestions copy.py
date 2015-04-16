"""
1. Find the point of intersection of two linked lists
"""
# I. Use 2 nested loops, compare each node with others.
# will need O(mn) time

# II. Mark visited nodes
# This will need modification to linked list structure. Has a visited flag
# will need O(m+n) time

# III. Get the longer list length of m, and the shorter n
# traverse the longer one d = m-n, and then traverse both in parallel
# O(m+n) time, O(1) space

# IV. Make cirvle in first list.
# Use two pointers to find loop in second list, remove the circle
# O(m+n) time, O(1) space

"""
2. Reverse a linked list
"""
# I. Iterative method
def reverse(head):
    if head is None or head.next is None:
        return head
    second = head.next
    third = second.next
    second.next = head
    head.next = None

    cur = third
    pre = second
    while cur is not None:
        nex = cur.next
        cur.next = pre
        pre = cur
        cur = nex
    head = pre
    return head

# II. Recursive method
def reverse(cur):
    if cur is None:
        return
    if cur.next is None:
        head = cur
        return
    reverse(cur.next)
    cur.next.next = cur
    # Set "old" next pointer to None
    cur.next = None

"""
3. Return the mth number in nth row in a pascal triangle
"""
# First we build the pascal triangle
triangle = []
for i in xrange(n+1):
    if i == 0:
        triangle.append([1])
    elif i == 1:
        triangle.append([1,1])
    else:
        ll = []
        for j in xrange(n+1):
            if j == 0 or j == n:
                ll.append(1)
            else:
                ll.append(triangle[i-1][j-1]+triangle[i-1][j])
        triangle.append(ll)
return triangle[n][m]

"""
4. Merge k sorted lists
"""
# Since list internaly in python is array, a list[1:] can be costy
# Could use a double-ended list instead
def merge(ll):


