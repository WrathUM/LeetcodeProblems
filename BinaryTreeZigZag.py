class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = [root]
        res = []
        while queue:
            l1 = []
            l2 = []
            for n in queue:
                l1.append(n.val)
                if n.left:
                    l2.append(n.left)
                if n.right:
                    l2.append(n.right)
            res.append(l1)
            queue = l2
        
        for i in range(len(res)):
            if i % 2 != 0:
                res[i] = reversed(res[i])
        
        return res
