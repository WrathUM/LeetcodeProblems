class Node(object):
    def __init__(self, key):
        self.key = key
        self.next = None
        self.down = None
        

class Skiplist(object):

    def __init__(self):
        self.levels = []
        prev = None
        for i in range(16):
            node = Node(-float('inf'))
            self.levels.append(node)
            if prev:
                prev.down = node
            prev = node
        
    def _iter(self, value):
        res = []
        l = self.levels[0]
        while l:
            while l.next and l.next.key < value:
                l = l.next
            res.append(l)
            l = l.down
            
        return res
        
    def search(self, target):
        """
        :type target: int
        :rtype: bool
        """
        last = self._iter(target)[-1]
        return last.next and last.next.key == target

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        res = self._iter(num)
        prev = None
        for i in range(len(res)-1, -1, -1):
            if i < len(res) - 1 and res[i].next == res[i + 1]:
                continue
            node = Node(num)
            node.next = res[i].next
            res[i].next = node
            node.down = prev
            prev = node
            propose = random.random()
            if propose > 0.5:
                break
            """
            30, 30, 50, 50, 70, 70
            
            """
        
    def erase(self, num):
        """
        :type num: int
        :rtype: bool
        """
        found = False
        res = self._iter(num)
        for i in range(len(res)):
            if res[i].next and res[i].next.key == num:
                res[i].next = res[i].next.next
                found = True
        return found


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
