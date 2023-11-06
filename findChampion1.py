def findChampion(self, grid: List[List[int]]) -> int:
        """
        [0,0,1]
        [1,0,1]
        [0,0,0]
        """
        n = len(grid)
        bestSum = 0
        bestIdx = -1
        for i in range(n):
            v = sum(grid[i])
            if v > bestSum:
                bestSum  = v
                bestIdx = i
                
        return bestIdx
