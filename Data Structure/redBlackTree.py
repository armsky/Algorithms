"""
- A red–black tree is a BST with an extra bit of data per node, its color, which can be either red or black.
It is a self-balancing binary search tree.
- The balancing of the tree is not perfect but it is good enough to allow it to guarantee searching in O(log n) time.

Time        Average     Worst
Access      O(log n)    O(log n)
Search      O(log n)    O(log n)
Insertion   O(log n)    O(log n)
Deletion    O(log n)    O(log n)

Space: O(n)

"""

"""
- A node is either red or black.
- The root is black. (This rule is sometimes omitted. Since the root can always be changed from red to black, but not necessarily vice versa, this rule has little effect on analysis.)
- All leaves (NIL) are black. (All leaves are same color as the root.)
- Every red node must have two black child nodes.
- Every path from a given node to any of its descendant NIL nodes contains the same number of black nodes.
"""
