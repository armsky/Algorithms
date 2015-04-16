#A priority queue is common implemented with a heap
"""
Basic operations:
    1. insert_with_priority
    2. pull_highest_priority_item
    3. peek

Difference between heap and priority queue:
    1. Heap is ONE implementation of a priority queue, and it's tree-based.
    2. Priority Queue is an abstract data structure.
"""
import heapq
    # heapq is a min heap, smallest item in the top

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        # heappop will return the smallest item
        return heapq.heappop(self._queue)[-1]

class Node:
    def __init__(self, data):
        self.data = data

class pq:
    def __init__(self):
        self.queue = []
        self.length = 0

    def sift(self, root, n):
        left = root*2 + 1
        right = root*2 + 2
        biggest = root
        if left < n and self.queue[left].data > self.queue[root].data:
            biggest = left
        if right < n and self.queue[right].data > self.queue[biggest].data:
            biggest = right
        if biggest != root:
            self.queue[root], self.queue[biggest] = self.queue[biggest], self.queue[root]
            root = biggest
            self.sift(root, self.length)

    def heapify(self):
        start = self.length/2 - 1
        while start >= 0:
            self.sift(start, self.length)
            start -= 1

    def insert(self, node):
        self.queue.append(node)
        self.length += 1
        if self.length == 1:
            return
        self.heapify()

    def pop(self):
        node = self.queue[0]
        non_node = Node(0)
        self.queue[0] = non_node
        for i in xrange(self.length/2 - 1):
            self.sift(i, self.length)
        return node

    def peek(self):
        return self.queue[0]

    def __str__(self):
        l = []
        for node in self.queue:
            l.append(str(node.data))
        return ' '.join(l)


p = pq()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

p.insert(node1)
print p
p.insert(node2)
p.insert(node3)
print p
p.insert(node4)
p.insert(node5)
p.insert(node6)
p.insert(node7)
print p
print p.pop().data
print p
print p.peek().data

