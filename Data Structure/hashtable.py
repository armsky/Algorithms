"""
A hashtable a structure for keeping a list of (key, value) pairs, where you can look up a value using the key that's associated with it.

the hashtable trades space for time. It creates many more buckets than the number of (key, value) pairs than it expects to store.

Time        Average     Worst
Access      -           -
Search      O(1)        O(n)
Insertion   O(1)        O(n)
Deletion    -           O(n)

Space: O(n)


- A collision is when two keys hash to the same index.
    When collision happens, Use a linked list to chain ellements in the same
    bucket.
- If all keys are known ahead of time, a "perfect hash function" can be used to create
    a perfect hash table that has no collisions. If minimal perfect hashing is used,
    every location in the hash table can be used as well.

"""
"""
Difference between hash table and hash map:
- map:
  1. no need to have a hash function, don't need to handle collision,
    O (log N) insert and lookup, insert key/data in sorted order. (If you need
    to find a max/min element, use map instead of hash table.)
  2. Map also stores key/value pair, so doesn't allocate huge space with empty
    slots.
- table:
  1. use a hash function to compute an key to it's bucket. doesn't insert
    hashed key/data in sorted order. It has O(1) lookup and insert
    in most cases.
  2. If the initial table size is not enough, need to resize the table, and
    transfet teh keys form old table to new table by a new hash function.

"""

# Implement it with just array
class HashEntry():

    def _init_(self, key, value):
        self.key = key
        self.value = value

    def get_key():
        return key

    def get_value():
        return value

class HashTable():
    TABLE_SIZE = 256

    def _init_(self):
        table = [[]] * TABLE_SIZE

    def hash(key):
        # hash function
        return hash_code

    def put(key, value):
        index = self.hash(key) % TABLE_SIZE
        if entry.value is None:
            return False
        else:
            table[index].append(HashEntry(key, value))
            return True

    def get(key):
        index = self.hash(key) % TABLE_SIZE
        if table[index] is None:
            return None
        for entry in table[index]:
            if entry.get_key() = key:
                return entry.get_value()
        else:
            return None
# If don't want multiple entries in the same bucket list, use Linear Probing, which will trie to find next empty slots in the array.
# table is one-dimension array now
def put(key, value):
    index = self.hash(key) % TABLE_SIZE
    while table[index] is not None and table[index].get_key() != key:
        index = (index+1) % TABLE_SIZE
    table[index] = HashEntry(key, value)

def get(key):
    index = self.hash(key) % TABLE_SIZE
    while table[index] is not None and table[index].get_key() != key:
        index = (index+1) % TABLE_SIZE
    return table[index].get_value()
