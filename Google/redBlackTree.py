"""
- A red–black tree is a self-balancing BST with an extra bit of data per node, its color, which can be either red or black.
- The balancing of the tree is not perfect but it is good enough to allow it to guarantee searching in O(log n) time.

Time        Average     Worst
Access      O(log n)    O(log n)
Search      O(log n)    O(log n)
Insertion   O(log n)    O(log n)
Deletion    O(log n)    O(log n)

Space: O(n)

"""
# Properties
"""
1. A node is either red or black.
2. The root is black. (This rule is sometimes omitted. Since the root can always be changed from red to black, but not necessarily vice versa, this rule has little effect on analysis.)
3. Every red node must have two black child nodes. (no two adjacent red nodes)
4. Every path from a given node to any of its descendant NIL nodes contains the same number of black nodes.
"""
# Comparison with AVL Tree
"""
The AVL trees are more balanced, but they may cause more rotations during insertion and deletion.
So if frequent insertions and deletions, then Red Black trees should be preferred. And if search is more frequent operation, then AVL tree .
"""
# Facts that can be proved using its properties:
"""
A RBT with n nodes has height <= 2log(n+1)
"""
# Insert: http://www.geeksforgeeks.org/red-black-tree-set-2-insert/
# Check the uncle to decide the appropriate case.
"""
1. Perform standard BST insertion and make the new node x color as RED
2. Do following if color of x's parent is not BLACK or x is not root:
    a) if x's uncle is RED (grand parent must have been black from property 4):
        i. change color of parent and uncle as BLACK
        ii. color of grand parent as RED
        iii. change x's grand parent as new x, repeat step 2 and 3
    b) if x's uncle is BLACK, , four configurations for x (similiar to AVL tree):
        i. LL case - right rotate g, swap color of g and p
        ii. LR case - left rotate p, apply LL, swap color of x and p
        iii. RL case - mirror of ii
        iv. RR case - mirror of i
3. If x is root, change color of x as BLACK (Black height complete tree increase by 1)
"""
def left_rotate(root, x):
    y = x.right
    x.right = y.left
    if x.right != None: # update parent pointer of x's right
        x.right.parent = x
    y.parent = x.parent # update parent pointer of y
    if x.parent == None:
        root = y # before x is root, now y is root
    elif x == x.parent.left: # if parent.left == x
        x.parent.left = y
    else: # parent.right == x
        x.parent.right = y
    y.left = x
    x.parent = y

def right_rotate(root, x):
    y = x.left
    x.left = y.right
    if x.left != None:
        x.left.parent = x
    y.parent = x.parent
    if x.parent == None:
        root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y
    y.right = x
    x.parent = y

# After a regular BST insert: http://ideone.com/PvEzCI
def insert_fix(root, z):
    while (z != root and z.parent.color == 'R' and z.color == 'B'):
        # store uncle as y
        if z.parent == z.parent.parent.right:
            y = z.parent.parent.right
        else:
            y = z.parent.parent.left
        # if uncle is RED
        if y.color == 'R':
            y.color == 'B'
            x.parent.color == 'B'
            x.parent.parent.color = 'R'
            z = z.parent.parent
        # uncle is BLACK, four cases: LL, LR, RL, RR
        else:
            # LL: swap color of p and g, right rotate g
            if z.parent == z.parent.parent.left and z == z.parent.left:
                swap(z.parent.color, z.parent.parent.color)
                right_rotate(root, z.parent.parent)
                z = z.parent # update new z
            # LR: left rotate p, swap color of z and g, right rotate g
            elif z.parent == z.parent.parent.left and z == z.parent.right:
                left_rotate(root, z.parent)
                z = z.parent
                # Leave the right rotate part to the next while loop
            # RR: swap color of g and p, left rotate of g
            elif z.parent == z.parent.parent.right and z == z.parent.right:
                swap(p.color, g.color)
                right_rotate(root, z.parent.parent)
                z = z.parent
            # RL: right rotate p, leave the rest to next loop
            else:
                right_rotate(root, z.parent)
                z = z.parent

    root.color = 'B'

# Delete
# Check color of sibling
"""
The main property that violates after insertion is two consecutive reds. In delete, the main violated property is, change of black height in subtrees as deletion of a black node may cause reduced black height in one root to leaf path.

When a black node is deleted and replaced by a black child, the child is marked as double black. The main task now becomes to convert this double black to single black.

1. Perform a BST delete. The successor is always a leaf or a node with only one child. Let v be the node deleted and u be the child that replace v.

2. simple case: if either u or v is RED, mark replaced child as BLACK

3. if both u and v are BLACK:
  1. color u as double black
"""
