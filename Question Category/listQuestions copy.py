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


