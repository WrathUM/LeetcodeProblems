 def isPalindrome(self, head: Optional[ListNode]) -> bool:
        res = []
        node = head
        while node:
            res.append(node.val)
            node = node.next
            
        n = len(res)
        for i in range(n):
            if res[i] != res[n-i - 1]:
                return False
        
        return True
      
"""
O(1) extra space
def isPalindrome(self, head: Optional[ListNode]) -> bool:
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
            
        node = head
        c = 0
        while node and c < length / 2:
            node = node.next
            c += 1
            
        secondStart = node
        
        prev = None
        cur = secondStart
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        secondStart = prev
        
        node1 = head
        node2 = secondStart
        
        while node1 and node2:
            if node1.val != node2.val:
                return False
            node1 = node1.next
            node2 = node2.next
            
        return True

"""
