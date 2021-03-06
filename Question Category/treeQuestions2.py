"""
1. Given a BST, write a function kthSmallest to find the kth smallest element in it.
"""
 # In-order traversal, O(N) time, O(k) space.
def kthSmallest(self, root, k):
    stack = []
    n = 0
    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            n += 1
            if n == k:
                return root.val
            root = root.right

"""
2.
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
1), return true, as there exist a root-to-leaf path.
2), return all paths
"""
def hasPathSum(self, root, sum):
        if not root:
            return False
        if not root.left and not root.right:
            if sum == root.val:
                return True
            else:
                return False
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

def pathSum(self, root, sum):
    result = []
    if root:
        stack = [root.val]
        self.dfs(root, sum-root.val, stack, result)
    return result

def dfs(self, root, sum, stack, result):
    if sum == 0 and not root.left and not root.right:
        result.append(stack)
    # Must use stack + [] to create new list (not stack.append())
    if root.left:
        self.dfs(root.left, sum-root.left.val, stack + [root.left.val], result)
    if root.right:
        self.dfs(root.right, sum-root.right.val, stack + [root.right.val], result)

"""
3. Count complete tree nodes.
Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
"""

class Solution:
    # @param {TreeNode} root
    # @return {integer}

    # Naive solution, will have TLE
    def countNodes(self, root):
        if not root:
            return 0
        import Queue
        q1 = Queue.Queue()
        q2 = Queue.Queue()
        q1.put(root)
        count = 1
        while not q1.empty():
            node = q1.get()
            if node:
                count += 1
            else:
                return count
            q2.put(node.left)
            q2.put(node.right)
            if q1.empty():
                q1, q2 = q2, q1

    # Use binary search to find how many nodes in last level.
    # Node number n = 2^h in last level, binary search takes O(log2 n) = O(h), each search also takes
    # O(h) from root to leaf, so total time complexity is O(h^2)
    def countNodes(self, root):
        if not root:
            return 0
        h = 0
        node = root
        while node.left:
            node = node.left
            h += 1
        l = 0
        r = 2 ** h - 1
        while l <= r:
            m = (l+r)/2
            if self.hasNode(root, m, h):
                l = m + 1
            else:
                r = m - 1
        return 2 ** h + r

    def hasNode(self, root, m, h):
        node = root
        for i in xrange(h-1, -1, -1):
            if m & 1 << i:
                node = node.right
            else:
                node = node.left
        return node is not None

    # Recursive solution
    # O(h^2)
    def countNodes(self, root):
        if not root:
            return 0
        l = 0
        r = 0
        lnode = root
        rnode = root
        while lnode.left:
            l += 1
            lnode = lnode.left
        while rnode.right:
            r += 1
            rnode = rnode.right
        if l == r:
            return (2 << l) -1
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) +1
"""
4. Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
"""
# Naive recursive solution, will have TLE
def lowestCommonAncestor(self, root, p, q):
    if not root:
        return None
    while root:
        if root == p or root == q:
            return root
        elif self.isDescendant(root.left, p) and self.isDescendant(root.left, q):
            root = root.left
        elif self.isDescendant(root.right, p) and self.isDescendant(root.right, q):
            root = root.right
        else:
            return root
    return None

def isDescendant(self, root, node):
    if not root:
        return False
    if root == node:
        return True
    else:
        return self.isDescendant(root.left, node) or self.isDescendant(root.right, node)

# Optimized recursive version
def lowestCommonAncestor(self, root, p, q):
    if root in (None, p, q):
        return root
    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)
    if not left:
        return right
    elif not right:
        return left
    else:
        return root

"""
5. Populate Next Right pointer in Each Node.
Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
"""
def connect(self, root):
    """
    :type root: TreeLinkNode
    :rtype: nothing
    """
    if not root:
        return
    pre = root
    node = None
    while pre.left:
        cur = pre
        while cur:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
            cur = cur.next

        pre = pre.left
# This works for all binary tree (not just perfect binary tree)
# But this is not using constant space
def connect(self, root):
    """
    :type root: TreeLinkNode
    :rtype: nothing
    """
    if not root:
        return
    so = [root]
    ss = []
    while any(so):
        for i in xrange(len(so)):
            if so[i] is not None:
                ss.append(so[i].left)
                ss.append(so[i].right)
                if i < len(so) -1:
                    so[i].next = so[i+1]
                else:
                    so[i].next = None
            else:
                ss.extend([None, None])
        so = ss
        ss = []
"""
6. Invert Binary Tree
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""
def invertTree(self, root):
    if root:
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    else:
        return None

"""
7. Binary Tree Maximum Path Sum
Given a binary tree, find the maximum path sum. The path may start and end at any node in the tree.
"""
def maxPathSum(self, root):
    # sinlgeSum could contain 0..n nodes
    # maxSum must have at least 1 node
    maxSum, singleSum = self.helper(root)
    return maxSum

def helper(self, root):
    if not root:
        # maxSum is globally max in tree, it must exist and must >= min_int
        return -sys.maxint-1, 0
    left = self.helper(root.left)
    right = self.helper(root.right)
    # singleSum must >= 0, because tree node may have value < 0
    singleSum = max(left[1] + root.val, right[1] + root.val, 0)
    maxSum = max(left[0], right[0], left[1] + right[1] + root.val)
    return maxSum, singleSum

