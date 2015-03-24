#A priority queue is common implemented with a heap
"""
Basic operations:
    1. insert_with_priority
    2. pull_highest_priority_item
    3. peek
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
