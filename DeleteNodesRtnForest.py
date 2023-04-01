# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        res = []
        
        def traverseDelete(node, to_delete, res):
            ls, rs = 0,0
            if node.left:
                ls, res = traverseDelete(node.left, to_delete, res)
                if ls == 1:
                    node.left = None
            if node.right:
                rs, res = traverseDelete(node.right, to_delete, res)
                if rs == 1:
                    node.right = None
            
            if node.val in to_delete:
                if node.left:
                    res.append(node.left)
                if node.right:
                    res.append(node.right)
                return 1, res
            
            return 0, res
        
        if root.val not in to_delete:
            res.append(root)
        state, res = traverseDelete(root, to_delete, res)
        
        return res
