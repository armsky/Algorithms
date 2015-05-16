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
# https://gist.github.com/werediver/4396488
import threading

class SingletonClass(object):
    __singleton_lock = threading.Lock()
    __singleton_instance = None

    @classmethod
    def instance(cls):
        if not cls.__singleton_instance:
            with cls.__sinleton_lock:
                if not cls.__singleton_instance:
                    # cls(): same thing as SingletonClass()
                    cls.__singleton_instance = cls()
        return cls.__singleton_instance

"""
4. Write a hadoop map/reduce
"""

"""
5. How to construct web Server
"""

"""
6. Design an effective data structure for a phone book, which allows searching by name and also searching by number.
(Similiar to design a auto-complete function)
"""
# Use Trie Tree


"""
7. Design a data structure with all the features of a stack, but with O(1) lookup for the max element currently in the structure.
"""
# Create two stacks, one is for storing all elements, the other one only store
# 'max element so far'
