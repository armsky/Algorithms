class Node():
    def __init__(self, data):
        self.data = data
        self.right = None
        self.down = None
        self.next = None

def flatten(head):
    s = []
    s.append(head)
    dummy = Node(None)
    cur = dummy
    while s:
        cur.next = s.pop()
        cur = cur.next
        if cur.right is not None:
            s.append(cur.right)
        if cur.down is not None:
            s.append(cur.down)
            cur.down = None
            cur.right = None
    return head

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)
node1.right = node2
node2.right = node3
node3.right = node4
node2.down = node5
node5.down = node8
node5.right = node6
node6.down = node9
node6.right = node7

head = flatten(node1)
while head.next is not None:
    print head.data
    head = head.next
print haed.data
