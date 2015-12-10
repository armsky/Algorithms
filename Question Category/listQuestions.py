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

# IV. Make circle in first list.
# Use two pointers to find loop in second list, remove the circle
# O(m+n) time, O(1) space

def getIntersectionNode(self, headA, headB):
    if not headA or not headB:
        return None
    a = headA
    b = headB
    while a and b and a!= b:
        a = a.next
        b = b.next
        if a == b:
            return a
        if not a: # circle it!
            a = headB
        if not b:
            b = headA
    return a

"""
2. Reverse a linked list
"""
# I. Iterative method
def reverse(head):
    pre = None
    cur = head
    while cur:
        nex = cur.next
        cur.next = pre
        pre = cur
        cur = nex
    return pre

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
2.5 Sum two linked lists
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""
# the digits are stored in reverse order
def addTwoNumbers(self, a, b):
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
    return dummy.next

# if the digits are stored in regular order
def addTwoNumbers(a1, b1):
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

"""
8. Partition list
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
Given 1->4->3->2->5->2->null and x = 3,
return 1->2->2->4->3->5->null
"""
def partition(self, head, x):
    if not head:
        return head
    ldummy = ListNode(0)
    rdummy = ListNode(0)
    left = ldummy
    right = rdummy
    while head:
        if head.val < x:
            left.next = head
            left = left.next
        else:
            right.next = head
            right = right.next
        head = head.next
    right.next = None # Important !!!
    left.next = rdummy.next
    return ldummy.next

"""
9. Linked List Cycle
Return the node where cycle begins, do not use extra space
"""
# Can use hashtable to solve this if extra space is allowed
def detectCycle(self, head):
    if not head or not head.next:
        return None
    a = head
    b = head.next
    while a != b:
        if not b or not b.next:
            return None
        a = a.next
        b = b.next.next
    while head != a.next:
        head = head.next
        a = a.next
    return head
