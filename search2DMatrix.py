def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m,n = len(matrix), len(matrix[0])
        i, j = m - 1, 0 
        while i >= 0 and j < n:
            # print(matrix[i][j])
            if target == matrix[i][j]:
                return True
            
            if j + 1 < n and matrix[i][j + 1] <= target:
                j += 1
            elif i - 1 >= 0:
                i -= 1
            else:
                return False

        return False
