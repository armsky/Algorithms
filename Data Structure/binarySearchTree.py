"""
Each node can have up to two child nodes.
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
The left and right subtree each must also be a binary search tree.
A unique path exists from the root to every other node.

Time        Average     Worst
Access      O(log n)    O(n)
Search      O(log n)    O(n)
Insertion   O(log n)    O(n)
Deletion    O(log n)    O(n)

Space: O(n)
"""
from sys import stdout
import Queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

class BST:
    def __init__(self):
        self.root = None

    def find_recursive(self, node, data):
        # General search by any given node
        if node == None or node.data == data:
            return node
        elif data < node.data:
            return self.find_recursive(node.left, data)
        else:
            return self.find_recursive(node.right, data)

    def find_iterative(self, node, data):
        # A iterative way
        current = node
        while node:
            if node.data == data:
                return current
            elif data < node.data:
                current = current.left
            else:
                current = current.right
        return current

    def search(self, data):
        # Search from root
        return self.find_recursive(root, data)

    def insert(self, node):
        if self.root == None:
            selt.root = node
            return True
        current = self.root
        while current:
            # Do not allow dups here
            if node.data == current.data:
                return False
            elif node.data < current.data:
                if current.left == None:
                    current.left = node
                    node.parent = current
                    return True
                else:
                    current = current.left
            else:
                if not current.right:
                    currnt.right = node
                    node.parent = current
                    return True
                else
                    current = current.right

    def delete(self, data):
        node = self.search(data)
        if node is None:
            return False
        else:
            self.remove_node(node)
            return True

    def remove_node(self, node):
        # If node has no children, just remove it.
        if not node.left and not node.right:
            self.replace_node(node, None)
        # The node has two children
        elif node.left and node.right:
            # successor is the smallest node that larger than node to be removed
            successor = node.right
            while successor.left:
                successor = successor.left
            # make current node equals to succesor, and remove successor
            node.data = successor.data
            self.remove_node(successor)
        # The node has left child only
        elif node.left:
            self.replace_node(node, node.left)
        elif node.right:
            self.replace_node(node, node.right)


    def replace_node(self, node, new):
        # special case: replace root
        if self.root == node:
            self.root = new
            return True
        parent = node.parent
        if parent.left and parent.left == node:
            parent.left = new
            return True
        elif parent.right and parent.right == node:
            parent.right = new
            return True
        else:
            return False

    # A simple callback function
    def printwithspace(i):
        stdout.write("%i ", % i)

    def inorder_recursive(self, node, visitor = printwithspace ):
        if not node:
            return
        self.inorder_recursive(node.left, visitor)
        self.visitor(node.data)
        self.inorder_recursive(node.right, visitor)

    def inorder_iterative(self, node, visitor = printwithspace):
        stack = []
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                self.visitor(node.data)
                node = node.right

    def preorder_recursive(self, node, visitor = printwithspace):
        if node is not None:
            self.visitor(node.data)
            self.preorder_recursive(node.left, self.visitor)
            self.preorder_recursive(node.right, self.visitor)

    def preorder_iterative(self, node, visitor = printwithspace):
        if node is not None:
            stack = [node]
            while stack:
                node = stack.pop()
                self.visitor(node.data)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)

    def postorder_recursive(self, node, visitor = printwithspace):
        if node is not None:
            self.postorder_recursive(node.left, self.visitor)
            self.postorder_recursive(node.right, self.visitor)
            self.visitor(node.data)

    def postorder_iterative(self, node, visitor = printwithspace):
        # Use two stacks is much easier
        if node is not None:
            temp = [node]
            stack = []
            while temp:
                node = temp.pop()
                stack.append(node)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            while stack:
                self.visitor(stack.pop().data)

    def levelorder_recursive(self, node, more=None, visitor = printwithspace):
        if node is not None:
            if more is None:
                more = []
            more += [node.left, node.right]
            self.visitor(node.data)
        if more:
            self.levelorder_recursive(more[0], more[1:], self.visitor)

    def levelorder_iterative(self, root, visitor = printwithspace):
        # Use two queues to store current level's nodes and next level's nodes
        if not root:
            return []

        import Queue
        q1 = Queue.Queue()
        q1.put(root)
        q2 = Queue.Queue()
        re = []
        temp = []
        while not q1.empty():
            node = q1.get()
            temp.append(node.val)
            if node.left is not None: q2.put(node.left)
            if node.right is not None: q2.put(node.right)
            if q1.empty():
                re.append(temp)
                temp = []
                q1, q2 = q2, q1
        return re
"""
The traversal above all use recursive or stack (O(n) space used)
Morris will only need O(1) space and O(n) time, (Each edge is traversed
at most 3 times and there are n-1 edges in a tree, hence the O(n). )
Benifits: don't need extra predecessor or successor pointer
"""
    def morris_inorder(self, root, visitor = printwithspace)):
        cur = root
        prev = None
        while cur is not None:
            # If left is none, print it
            if cur.left is None:
                self.visitor(cur.data)
                cur = cur.right
            else:
                # Find predecessor
                prev = cur.left
                while prev.right is not None and prev.right != cur:
                    # untill prev is the predecessor of root
                    prev = prev.right
                # make prev.right -> cur, and cur = cur.left
                if prev.right is None:
                    prev.right = cur
                    cur = cur.left
                # restore the tree (right point to none), update cur
                else:
                    prev.right = None
                    self.visitor(cur.data)
                    cur = cur.right

    # Only one line different: the print
    def morris_preoder(self, root, visitor = printwithspace)):
        cur = root
        prev = None
        while cur is not None:
            if cur.left is None:
                self.visitor(cur.data)
                cur = cur.right
            else:
                prev = cur.left
                while prev.right is not None and prev.right != cur:
                    prev = prev.right
                if prev.right is None:
                    self.visitor(cur.data) # the only difference
                    prev.right = cur
                    cur = cur.left
                else:
                    prev.right = None
                    cur = cur.right

