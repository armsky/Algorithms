"""
1. Return the occurrence of each letter of a given string in alphabetical order
"""
# Use dict to store occurrence of each letter, and sort the key,value pair
for k, v in sorted(table.items()):
    print k, v


"""
2. Use Array to implement a hashtable
"""
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


"""
If don’t want multiple entries in the same bucket list, use Linear Probing, which will trie to find next empty slots in the array. Revise get and put functions as below.
"""
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
