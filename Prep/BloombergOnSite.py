"""
1. There is a linked list in which each node has a pointer to next node and some random node. Write a code that clones such linked list in O(n) time.
"""
# Remember a node's random can point to it self
# so the table shoule have:: key: original node, value: clone node
# But it will lose 'next' in while loop, so we need extra 'pre' node
def clone(head):
    if not head:
        return None
    table = {}
    dummy = RandomListNode(0)
    node = RandomListNode(head.label)
    dummy.next = node
    pre = dummy
    while head:
        if head in table:
            node = table[head]
        else:
            node = RandomListNode(head.label)
            table[head] = node
        pre.next = node
        if head.random:
            if head.random in table:
                node.random = table[head.random]
            else:
                node.random = RandomListNode(head.random.label)
                table[head.random] = node.random
        head = head.next
        pre = pre.next
    return dummy.next
"""
2.  Design a system which represents a flight radar. There are planes which are flying in every direction (without any predictable route) and a radar that can track their location. System should have a function that returns location of ten closest to the radar planes every time it is called. The function is called very frequently by clients and should return data immediately.
"""
# A special heap (size of 10) with plane number and it's distance.
# If a plane changes it's distance, the system will try to update the heap
# If a new plane has less distance, just update the heap by poping the root
# If a plane already in head changes it's distance, heapify the heap
"""
3. Implement multiple-readers/single-writer lock (multithreading)
"""

class RWLock:

    # A simple RWlock: Multiple readers can hold the lock simultaneously, XOR one writer.

    def read_lock():
        mutex.lock()
        while (writer):
            wait()
        reader += 1
        mutex.unlock()

    def read_unlock():
        mutex.lock()
        reader -= 1
        if reader == 0:
            notify_all()
        mutex.unlock()

    def write_lock():
        mutex.lock()
        while reader>0 or writer:
            wait()
        writer = 1
        mutex.unlock()

    def write_unlock():
        mutex.lock()
        writer = 0
        notify_all()
        mutex.unlock()

# Some drawbacks for this implementation
# 1. No priority, reader will starve writer, with priority, writer will starve reader. Maybe should random choose reader/writer
# 2. No order, could use a queue for readers


"""
4. There is a binary tree in which each node has three pointers: pointer to left child, pointer to right child and pointer to next node on the same level. Write a code to clone such tree.
"""
class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
# First clone tree without right pointer
def clone(root):
    if not root:
        return None
    node = TreeLinkNode(root.val)
    node.left = self.clone(root.left)
    node.right = self.clone(root.right)
    return node
# The populate the right pointer
# IF the tree is perfect BT
def connect(root):
    if not root:
        return None
    pre = root
    cur = None
    while pre.next:
        cur = pre
        while cur:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
            cur = cur.next
        pre = pre.left
# If not perfect tree
def connect(self, root):
    head = root # Left most node of Lower level
    pre = None # previous node of Lower level
    cur = None # current node of upper level
    while head:
        cur = head
        head = None
        pre = None
        while cur:
            if cur.left:
                if pre:
                    pre.next = cur.left
                else:
                    head = cur.left
                pre = cur.left
            if cur.right:
                if pre:
                    pre.next = cur.right
                else:
                    head = cur.right
                pre = cur.right
            cur = cur.next

"""
5. Given a real-time list of traded stocks, need to get the last N (arbitrary) unique traded stocks. Write addTrade(string ticker) and getLastNUnique(int n) functions with efficient runtime.
"""
class StockTrack():

    def __init__(self):
        self.table = {}
        self.dll = DoublyLinkedList()

    def addTrade(self, ticker):
        if ticker in self.table:
            self.dll.delete(ticker)
            self.dll.add_frount(ticker)
        else:
            table[ticker] = 1
            self.dll.add_front(ticker)

    def getLastNUnique(self, n):
        re = []
        cur = self.dll.head
        while cur and n > 0:
            re.append(cur)
            cur = cur.next
        return re

