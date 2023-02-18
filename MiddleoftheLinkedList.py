def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node1 = head
        node2 = head
        
        while node2.next and node2.next.next:
            node1 = node1.next
            node2 = node2.next.next
            
        if node2.next:
            node1 = node1.next
            
        return node1  
