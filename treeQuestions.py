"""
1. Given the root of a binary search tree and 2 numbers min and max, trim the tree such that all the numbers in the new tree are between min and max (inclusive). The resulting tree should still be a valid binary search tree.
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
