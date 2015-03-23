"""
FIFO.
dequeue <- HEAD --- TAIL <- enqueue

BASIC OPERATIONS:
1. enqueue(x): add an item at the tail
2. dequeue: remove the item at the head
3. peek: return the item at the head (without removing it)
4. size: return the number of items in the queue
5. isEmpty: return whether the queue has no items
"""
###############
"""
# Implement a queue by using two stacks (use list as stack)
1. Enqueue:
    -Push the new element onto inbox (stack 1)
2. Dequeue:
    -If outbox is empty, refill it by popping each element from inbox
     and pushing it onto outbox (stack 2). If not empty, pop
    -Pop and return the top element from outbox
"""
class Queue():
    inbox = list()
    outbox = list()

    def enqueue(item):
        inbox.append(item)

    def dequeue():
        if not len(outbox):
            while len(inbox) != 0:
                outbox.append(inbox.pop())
        return outbox.pop()

    def peek():
        if not len(outbox):
            while len(inbox) != 0:
                outbox.append(inbox.pop())
        return outbox[-1]
