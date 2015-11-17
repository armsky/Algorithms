"""
1.
Input : {"tea", "eat", "ate", "run","urn","cool","school"}
Output : {{"tea", "eat", "ate"},{"run","urn"}}
"""
# set and list are unhashable
def category(words):
    table = {}
    result = []
    for word in words:
        # Sort the string as list, and use string as hash key
        chars = str(sorted(list(word)))
        if chars in table:
            table[chars].append(word)
        else:
            table[chars] = [word]
    for word_list in table.values():
        if len(word_list) > 1:
            result.append(word_list)
    return result

words = ["tea", "eat", "ate", "run","urn","cool","school"]
print category(words)

"""
2.
input:

       -----------
      |          |

A---->B--->C---->D---->E
|          ^
|          |
------------

output:

        ------------
       |            |
A'---->B'--->C'---->D'---->E''
|            ^
|            |
 ------------

 struct node
{
    node * next;
    node * jump;
    int val
}
 """
def copy_list(a):
    b = Node(a)
    heada = a
    headb = b
    # Copy this list without jump pointer
    while a.next:
        b.next = Node(a.next.val)
        a = a.next
        b = b.next
    a = heada
    b = headb
    while a:
        if a.jump:
            table[a.jump.val] = b
        if b.val in table:
            table[b.val].jump = b
        a = a.next
        b = b.next
    return headb


"""
3. Clone graph
Return a deep copy of graph
"""

"""
4. Continuous sequence with the largest sum
Example: input[2,-8,3,-2,4,-10] -> output: 5 (from the continuous sequence 3,-2,4).
"""

"""
5. shortest path to Good point.
gave a matrix, (B means cannot go through)
000
BGG
G00

calculate the shortest path between each 0 to G, so result will be

211
BGG
G11
"""
import Queue

def shortest(matrix):
    if not matrix:
        return None
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == "0":
                q = Queue.Queue()
                q.put([i,j])
                while q:
                    i, j = q.get()
                    mark(matrix, i, j, m, n, q)
    print matrix

def calculate(matrix, i, j, m, n, q):
    if matrix[i][j] == "G":
        return "1"
    else:
        return str(int(matrix[i][j]) + 1)
    if i - 1 >= 0 and matrix[i-1][j] == "0":
        calculate(matrix, i-1, j, m, n, q)

def mark(matrix, i, j, m, n, q):
    to_mark = []
    if i - 1 >= 0:
        to_mark.append([i-1, j])
    if j - 1 >= 0:
        to_mark.append([i, j-1])
    if j + 1 < n:
        to_mark.append([i, j+1])
    if i + 1 < m:
        to_mark.append([i+1, j])
    print to_mark
    for cor in to_mark:
        if matrix[cor[0]][cor[1]] != "B" and matrix[cor[0]][cor[1]] != "G":
            if matrix[cor[0]][cor[1]] == "0":
                q.put([cor[0], cor[1]])
            if matrix[i][j] == "G":
                matrix[cor[0]][cor[1]] == "1"
            else:
                if int(matrix[cor[0]][cor[1]]) > int(matrix[i][j]) + 1:
                    matrix[cor[0]][cor[1]] = str(int(matrix[i][j]) + 1)

matrix = ["000",
"BGG",
"G00"
]
#print shortest(matrix)

"""
6. Sum of two linked list
7->8 + 2->2 = 1->0->0
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# reverse two linked lists, sum them up and reverse back
def list_sum(a1, b1):
    a = reverse(a1)
    b = reverse(b1)
    dummy = c = ListNode(0)
    carry = 0
    while a or b or carry:
        if a:
            carry += a.val
            a = a.next
        if b:
            carry += b.val
            b = b.next
        carry, val = divmod(carry, 10)
        c.next = ListNode(val)
        c = c.next
    return reverse(dummy.next)

def reverse(a):
    pre = None
    cur = a
    while cur:
        nex = cur.next
        cur.next = pre
        pre = cur
        cur = nex
    return pre

#a = ListNode(1)
#a.next = ListNode(2)
#a.next.next = ListNode(9)
#b = ListNode(2)
#b.next = ListNode(1)
#
#nh = list_sum(a, b)
#while nh:
#    print nh.val
#    nh = nh.next

"""
7. check parentheses is balanced
"""
# Remember if all are right parentheses
# stack will still be empty at last
