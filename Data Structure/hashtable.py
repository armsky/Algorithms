"""
A hashtable a structure for keeping a list of (key, value) pairs, where you can look up a value using the key that's associated with it.

the hashtable trades space for time. It creates many more buckets than the number of (key, value) pairs than it expects to store.

Time        Average     Worst
Access      -           -
Search      O(1)        O(n)
Insertion   O(1)        O(n)
Deletion    -           O(n)

Space: O(n)

"""
