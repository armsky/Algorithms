def GiveBreadth(root, level):
    if not root:
        return 0
    import Queue
    q1 = Queue.Queue()
    q2 = Queue.Queus()
    q1.put(root)
    count = 1
    cur_lev = 1
    while q1:
        if cur_lev == level:
            return count
        count = 0
        while q1:
            node = q1.get()
            count += 1
            if node.left:
                q2.put(node.left)
            if node.rigth:
                q2.put(node.right)

        q1, q2 = q2, q1
        cur_level += 1

class LRUCache:

    def __init__ (self, capacity):
        self.capacity = capacity
        self.l  = []
        self.table = {}

    def getLatest(self):
        if self.l:
            return self.l[0]
        else:
            return None

    def updateItem(self, key, value):
        if key in self.table:
            old_value = table[key]
            if old_value in self.l:
                index = self.l.index(old_value)
                table[key] = value
                if index != 0:
                    self.l[1:index+1] = self.l[0:index]
                    self.l[0] = value
            else:
                self.l[1:-1] = self.l[0:-2]
                self.l[0] = value
        else:
            table[key] = value
            self.l[1:-1] = self.l[0:-2]
            self.l[0] = value


    def getItem(self, key):
        if key in self.table:
            value = table[key]
            if value in self.l:
                return table[key]
        return None
