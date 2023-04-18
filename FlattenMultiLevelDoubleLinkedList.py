"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return head
        
        res = []
        def traverse(node):
            if not node:
                return
            res.append(node.val)
            if node.child:
                traverse(node.child)
            if node.next:
                traverse(node.next)
                
        traverse(head)
        
        # reconstruct flattened list
        front = Node(res[0], None, None, None)
        prev = front
        for val in res[1:]:
            newNode = Node(val, prev, None, None)
            prev.next = newNode
            prev = newNode
        
        return front
