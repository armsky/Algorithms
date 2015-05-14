"""
1. Implement a data structure to support dynamic insertion,
deletion of intervals. Overlapping intervals should be merged.
"""

"""
2. Implement a LRU Cache
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
"""
class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.cl = list()
        self.table = {}

    # @return an integer
    def get(self, key):
        if key in self.table:
            self.cl.remove(self.table[key])
            self.cl.append(self.table[key])
            return self.table[key]
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key not in self.table.keys():
            self.table[key] = value
            self.cl.append(self.table[key])
            if len(self.cl) > self.capacity:
                # Find the value:cl[0] corresponding key in table, and delete it too
                for k, v in self.table.items():
                    if v == self.cl[0]:
                        del self.table[k]
                        break
                del self.cl[0]
        else:
            self.cl.remove(self.table[key])
            self.table[key] = value
            self.cl.append(self.table[key])
"""
3. Thread safe singleton pattern
"""


"""
4. Write a hadoop map/reduce
"""

"""
5. How to construct web Server
"""
