"""
         1
        / \
       /   \
      /     \
     2       3
    / \     /
   4   5   6
  /       / \
 7       8   9
The correct output should look like this:
preorder:    1 2 4 7 5 3 6 8 9
inorder:     7 4 2 5 1 8 6 9 3
postorder:   7 4 5 2 8 9 6 3 1
level-order: 1 2 3 4 5 6 7 8 9

"""
# pre-order, in-order, and post-order tree traversal are called Depth First Search (DFS),
# since they visit the tree by proceeding deeper and deeper until it reaches the leaf nodes.
# Usually use recursion, or use _stack_ to simulate recursion by using iterative methods

# level-order traversal is Breadth First Search (BFS), since it visits the nodes level by level.

#++++++++++++++++++\

# Find the maximum height (depth) of a Binary Tree
def maxHeight(node):
    if node is None:
        return 0
    left_height = maxHeight(node.left)
    right_height = maxHeight(node.right)
    if left_height > right_height:
        return left_height + 1
    else:
        return right_height + 1

def max_iterative(node):
    # Any DFS could be modified to solve this problem
    # Or use BFS, record how many levels
    stack = []
    height = 0
    while node or stack:
        if node:
            stack.append(node)
            if len(stack) > height:
                height = len(stack)
            node = node.left
        else:
            node = stack.pop()
            node = node.right
    return height

# Find longest path of two leaves (diameter)
def diameter(node):
    if node is None:
        return 0
    lheight = maxHeight(node.left)
    rheight = manHeight(node.right)

    ldiameter = diameter(node.left)
    rdiameter = diameter(node.right)

    return max(lheight+rheight+1, max(ldiameter, rdiameter))

# Serialize and Deserialize (a preorder way)
def serialize(node):
    if node == None:
        return
    visit(node.value)
    serialize(node.left)
    serialize(node.right)

def deserialize(a):
    if a is None:
        return
    if a[0] is None:
        return None
    node = Node(a[0])
    a = a[1:] # Since list has no has_next function
    node.left = deserialize(a)
    node.right = deserialize(a)
    return node

