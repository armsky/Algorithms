"""
1. Serialize and Deserialize
Suppose each node has n children
"""
def serialize(node):
    if node == None:
        return
    array.append(node.key)
    for i in xrange(n):
        if node.child[i] is not None:
            serialize(node.child[i])
    return array

def deserialize(a):
    if a is None:
        return
    if a[0] is None
        return None
    node = Node(a[0])
    for i in xrange(n):
        node.child.append(deserialize(a))
    return node
