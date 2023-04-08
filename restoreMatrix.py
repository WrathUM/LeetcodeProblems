def restoreMatrix(self, rowSum, colSum):
        """
        :type rowSum: List[int]
        :type colSum: List[int]
        :rtype: List[List[int]]
        """
        numCols = len(colSum)
        numRows = len(rowSum)
        
        matrix = [[0] * numCols for _ in range(numRows)]
        
        for i in range(numRows):
            matrix[i][0] = rowSum[i]
            
        """
        [[3,0]
         [8,0]]
        """
        
        for i in range(numCols - 1):
            cSum = 0
            for j in range(numRows):
                if cSum < colSum[i]:
                    if cSum + matrix[j][i] > colSum[i]:
                        diff = colSum[i] - cSum
                        matrix[j][i + 1] = matrix[j][i] - diff
                        matrix[j][i] = diff
                        cSum += diff
                    else:  
                        cSum += matrix[j][i]
                else:
                    matrix[j][i + 1] = matrix[j][i]
                    matrix[j][i] = 0
                    
        return matrix
