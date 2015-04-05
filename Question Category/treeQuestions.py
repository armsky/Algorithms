"""
1. Given the root of a binary search tree and 2 numbers min and max,
trim the tree such that all the numbers in the new tree are between min and max (inclusive).
The resulting tree should still be a valid binary search tree.
"""
# Remove all nodes but between in that range by performing a post-order traversal.
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
# Return counter == n/2 (odd) or the average of data of
# (n-1)/2 + data of n/2
def findMedian(root):
    if root is None:
        return None
    cur = root
    prev = None
    count = 0
    # suppose we already know the tree has n nodes
    while cur is not None:
        if cur.left is None:
            cur = cur.right
            count += 1
        else:
            prev = cur.left
            while prev is not None and prev != cur:
                prev = prev.right
            if prev.right == None:
                prev.right = cur
                cur = cur.left
            else:
                prev.right = None
                count += 1
                cur = cur.right
        #
        if count == n/2:
            if n%2 == 1:
                return cur.data
            else:
                return (prev.data + cur.data)/2

"""
4. How to find median in free running stream of random numbers.
"""
# I.- Create a balanced BST of first K numbers
#   - Find median of first K numbers
#   - Inset new number in BST and delete the first number of BST
#   - If the inseted on is greater that median, return the successor of median
#   - If less than median, return the predecessor of median

# II. - Create two heaps, one max-heap, one min-heap
#     - max-heap store smallest half elements, min-heap store larger half
#     - If the new element greater that top of min-heap, insert it to min-heap with O(log n)
#     - If less than top of max-heap, insert to max-heap with O(log n)
#     - If two heaps differs by more than 1, pop the longer heap and insert to the other,
#       which is O(log n) + O(log n)
#     - If the element is between the values of the two tops, insert it to the shorter
#       one, or if either one if they are equal
def addNewNumber(num):
    if minHeap.size() == maxHeap.size()
        if minHeap.peek() is not None and num > minHeap.peek():
            maxHeap.push(minHeap.pop())
            minHeap.push(num)
        else:
            maxHeap.push(num)
    else:
        if num < maxHeap.peek():
            minHeap.push(maxHeap.pop())
            maxHeap.push(num)
        else:
            minHeap.push(num)

def getMedian():
    if maxHeap is None and minHeap is not None:
        return maxHeap.peek()
    elif minHeap is None and maxHeap is not None:
        return minHeap.peek()
    elif minHeap.size() == maxHeap.size():
        return (minHeap.peek() + maxHeap.peek())/2
    else:
        return maxHeap.peek()

"""
5. find a sibling (cousin) of a given node of a binary tree. Check if two nodes are siblings.
- Sibling: nodes that has same parent.
- Cousin: nodes that at same level and have different parents.
"""

def isSibling(node, a, b):
    if node is None:
        return False
    return (node.left == a and node.right == b) or
            (node.right == a and node.left == b) or
            isSibling(node.left, a, b) or
            isSibling(node.right, a, b)

def getLevel(root, target, lev):
    # Find the level of node 'target'
    if root is None:
        return 0
    if root == targt:
        return lev
    l = getLevel(root.left, target, lev + 1)
    if l != 0:
        return l
    l = getLevel(root,right, target, lev + 1)
    return l

def isCousin(node, a, b):
    if (level(node, a, 1) == level(node, b, 1)) and
        isSibling(node, a, b) is False: # if they are siblings, they are not cousin
        return True
    else:
        return False

"""
6. check if a binary tree is BST or not
"""
# WRONG method: check each node that left < node < right

# I. Keeping track of the min and max to make min < data < max
# O(n) time, O(1) auxiliary space
def inRange(node, minV, maxV):
    if node is None:
        # Let empty tree be BST
        return True
    if node.data <= minV or node.data >= maxV:
        return False
    # Recursive check the subtree, and tight the range
    return inRange(node.left, minV, node.data) and
            inRange(node.right, noda.data, maxV)

def isBST(root):
    maxV = sys.maxint
    minV = -sys.maxint - 1
    return inRange(root, minV, maxV)

# II. Inorder traversal and store the result to temp array
# If the array is sorted in ascending order, is BST
# O(n) time.
def isBST(root):
    stack = []
    node = root
    while node is not None or stack != []:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if node.data >= stack[-1].data:
                return False
            node = node.right
    return True

"""
7. Design a data structure to implement a phone book. Can search by name or number
Use Trie:
"""
class Trie:
    def __init__(self):
        self.root = {}

    def add(self, name, number):
        # Add name/number to the Trie
        node = self.root
        for char in name:
            if char not in node:
                node[char] = {}
            node = node[char]
        node["Number"] = number

    def find(self, prefix):
        # Return node after consuming given prefix
        node = self.root
        for char in prefix:
            if char no in node.keys():
                return None
            node = node[char]
        return node
# Then a hashtable for numbers as key, names as value
