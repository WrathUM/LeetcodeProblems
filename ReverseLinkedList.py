def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        values = []
        def recurse(node, vals):
            if not node:
                return

            vals.append(node.val)

            if node.next:
                recurse(node.next, vals)
            
            node.val = vals.pop(0)

        recurse(head, values)

        return head
