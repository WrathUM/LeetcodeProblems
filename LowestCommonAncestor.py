def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        pAncestor = defaultdict(int)
        qAncestor = defaultdict(int)
        
        def traverseTree(node, val, level, ancestor):
            if not node:
                return False

            
            if node == val:
                ancestor[node] = level
                return True
            if traverseTree(node.left, val, level + 1, ancestor):
                ancestor[node] = level
                return True
            if traverseTree(node.right, val, level + 1, ancestor):
                ancestor[node] = level
                return True
            return False
        
        traverseTree(root, p, 0, pAncestor)
        traverseTree(root, q, 0, qAncestor)
        
        lowestLevel = 0
        descedentVal = root
        for k in pAncestor.keys():
            if k in qAncestor:
                if lowestLevel < pAncestor[k]:
                    lowestLevel = pAncestor[k]
                    descedentVal = k
        
        return descedentVal
