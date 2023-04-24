class node(object):
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.left = None
        self.right = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = defaultdict(node)
        self.front = node(0,0)
        self.back = node(0,0)
        self.front.right = self.back
        self.back.left = self.front

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            prev, nxt = node.left, node.right
            prev.right = nxt
            nxt.left = prev
            
            if node == self.back.left:
                self.back.left = prev
                prev.right = self.back
            
            self.nodeToFront(node)
            
            return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.cache[key].val = value
            self.get(key)
            return
        
        if len(self.cache.keys()) + 1 > self.capacity:
            # evict
            prev = self.back.left
            print(prev.key, prev.val)
            self.back.left = prev.left
            prev.left.right = self.back
            self.cache.pop(prev.key)
            
        
        newNode = node(key, value)
        self.nodeToFront(newNode)
        self.cache[key] = newNode
        
    def nodeToFront(self, node):
        node.right = self.front.right
        node.left = self.front
        self.front.right.left = node
        self.front.right = node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
