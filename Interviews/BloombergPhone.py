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


words = ["tea", "eat", "ate", "run","urn","cool","school"]
print category(words)
