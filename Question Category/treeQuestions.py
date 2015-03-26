"""
1. Given the root of a binary search tree and 2 numbers min and max,
trim the tree such that all the numbers in the new tree are between min and max (inclusive).
The resulting tree should still be a valid binary search tree.
"""
# Remove all nodes bot between in that range by performing a post-order traversal.
# Must be post-order to ensure it's a bottom-up
def trimBST(node, minVal, maxVal):
    if not node:
        return
    node.left = trimBST(node.left, minVal, maxVal)
    node.right = trimBST(node.right, minVal, maxVal)
    if minVal <= node.data <= maxVal:
        return node
    elif node.data < minVal:
        return node.right
    else:
        return node.left


"""
2. Create a balanced binary search tree from a
  - sorted Linked List
  - sorted array of integers
"""
# From a sorted Linked List
# I. From root to leaf, get the middle in list and make it root
# The do same for the left and right half.
# O(n Log n), n is list number.
def constrctTree(treeroot, listroot, n):
    if listhead is None:
        return None
    else:
        treeroot = listhead[n/2]
        treeroot.left = constructTree(listhead, n/2)
        treeroot.right = constructTree(listhead[n/2 +1], n/2)
        return treeroot

# II. From leaf to root. build the tree based on the list sequence
# Take n/2 nodes to build left tree recursively, then connect the tree
# root to the left subtree, and last recursively build the right subtree.
# O(n) time
def constructTree(listhead, n):
    if n <= 0:
        return None
    leftnode = constructTree(listhead, n/2)
    # subtree's root
    treeroot = TreeNode(listhead.data)
    treeroot.left = leftnode
    listhead = listhead.next
    # Must also subract the root, so -1 at last
    treeroot.right = constructTree(listhead, n - n/2 -1)

#===================
# From a sorted Array
# I. Root to leaf, make middle as root, do same to left and right
# O(n) time
def constructTree(array, tree):
    if array is not None:
        n = len(array)
        tree = array[n/2]
        tree.left = constructTree(array[0:n/2])
        tree.right = constructTree(array[n/2 +1 :])
        return tree
    else:
        return None

"""
3. Find the median in a BST, use no extra memory
"""
# Use Morris Inorder, count each node that visited
# Return counter == n/2 (even) or (n+1)/2 (odd)

"""
4. How to find median in free running stream of random numbers.
"""
