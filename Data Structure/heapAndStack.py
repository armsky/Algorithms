# Stack
# FILO, has size limits, no need to manage the memory yourself,
#  variables are allocated and freed automatically
# Local variable only
class Stack():
    def __init__(self):
        self.items = []

    def pop(self):
        return self.items.pop()

    def push(self, item):
        self.items.append(item)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[len(self.items)-1]


# Heap
# No size restriction, heap variables are global in scope
