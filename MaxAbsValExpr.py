def maxAbsValExpr(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        points = []
        for i, (x,y) in enumerate(zip(arr1, arr2)):
            points.append((
                x + y + i, 
                x + y - i, 
                x - y + i, 
                x - y - i
            ))
            
        return max(max(dim) - min(dim) for dim in zip(*points))
