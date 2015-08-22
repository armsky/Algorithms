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
Could have extended question in distributed system
"""
# a. Like MergeSort, divide k lists to k/2 and so on, until there are
#       only two lists, recursively merge them
# k lists, each list has n elements, O(nk log k) time, O(log k) stack space
def merge_lists(ll):
    k = len(ll)
    if k == 0:
        return None
    return helper(ll, 0, k-1)

def helper(lists, l, r):
    if l < r:
        m = (l+r)/2
        return merge(helper(lists, l, m), helper(lists, m+1, r))
    return lists[l]

def merge(a, b):
    # a and b are list nodes
    dummy = Node()
    if a is not None:
        dummy.next = a
    else:
        dummy.next = b
    cur = dummy
    while a is not None and b is not None:
        if a.val < b.val:
            a = a.next
        else:
            next = b.next
            cur.next = b
            b.next = a
            b = next
        cur = cur.next
    if a is not None:
        cur.next = a
    if b is not None:
        cur.next = b
    return dummy.next

# b. Maintain a min-heap size as k, each time pop the top element(t) to the
#       the result, t = t.next, and maintain the heap
# O(nk log k) time, O(k) space
def merge_lists(ll):
    heap = heapq()
    for l in ll:
        if l is not None:
            heappush(heap, l)
    dummy = Node(0)
    runner = dummy
    while heap is not None:
        cur = heappop(heap)
        runner.next = cur
        runner = runner.next
        # Maintain the heap
        if cur.next is not None:
            heappush(heap, cur.next)
    return dummy.next
"""
5. Given a list of size n and possible values from 0 to n. Find the missing number
"""
# (Sum of 0..n) - (Sum of list)

"""
6. Flatten a 2D linked list.
A node contains 3 parameters namely, data , pointer to right, pointer to down . The aim of the function is to flatten the linkedlist.

Ex: 1-->2-->4
        |
        V
        3

Answer is 1-->2-->3-->4

Ex: 1 --> 2--> 3--> 4
               |
               5-->6-->7
               |   |
               8   9

Answer is 1-->2->5 -> 8 -> 6->9 ->7-> 3-> 4
"""
#a. use a stack
def flatten(head):
    s = []
    s.append(head)
    dummy = Node(None)
    cur = dummy
    while s:
        cur.next = s.pop()
        cur = cur.next
        if cur.right is not None:
            s.append(cur.right)
        if cur.down is not None:
            s.append(cur.down)
            cur.down = None
            cur.right = None
    return head
#b. recursively
def flatten(head):
    if head is None:
        return head
    next_node = head.right
    if head.down is not None:
        head.next = flatten(head.down)
        head.down = None
        pointer = head.right
        while pointer.right is not None:
            pointer = pointer.right
        pointer.next = next_node
    flatten(next_node)
    return head

"""
7. Sort a linked list using insertion sort.
"""
def insertionSortList(self, head):
    if not head or not head.next:
        return head
    # Must maintain three pointers, pre, cur and nex
    # pre points to the sorted list's fake head
    # cur points to the node to be inserted
    # nex points to the next node to be inserted
    newhead = ListNode(0)
    cur = head
    # To avoid Time Limit Exceeded, make this optimization
    sortedEnd = head
    while cur:
        nex = cur.next

        if sortedEnd.val < cur.val:
            sortedEnd.next = cur
            cur.next = None
            sortedEnd = cur
        else:
            pre = newhead
            while pre.next and pre.next.val <= cur.val:
                pre = pre.next
            # This will break the list into two parts
            cur.next = pre.next
            pre.next = cur
        cur = nex
    return newhead.next
