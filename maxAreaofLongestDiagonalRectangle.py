class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        bestDiag = 0
        bestArea = 0
        for i in range(len(dimensions)):
            diag = sqrt(dimensions[i][0]**2 + dimensions[i][1]**2)
            if diag > bestDiag:
                bestDiag = diag
                bestArea = dimensions[i][0] * dimensions[i][1]
            elif diag == bestDiag and bestArea < dimensions[i][0] * dimensions[i][1]:
                bestArea = dimensions[i][0] * dimensions[i][1]
            
        return bestArea
                
                
