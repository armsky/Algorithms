"""
LIFO
It has size limits, no need to manage the memory yourself,
variables are allocated and freed automatically
Local variable only
"""

# Using lists as stack
# push = list.append()
# pop = list.pop()
# isEmpty = return size==0
# size = len()
# peek = return list[-1]

"""
Implement a stack by using two queues.

- push:
enqueue in queue1
- pop:
while size of queue1 is bigger than 1, pipe dequeued items from queue1 into queue2
dequeue and return the last item of queue1, then switch the names of queue1 and queue2
"""
