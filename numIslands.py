def numIslands(self, grid: List[List[str]]) -> int:
        numRow = len(grid)
        numCol = len(grid[0])
        isVisited = set()
        res = 0
        
        def findIsland(i, j):
            if i < 0 or j < 0 or i >= numRow or j >= numCol:
                return 0
            
            if (i,j) in isVisited:
                return 0
            else:
                isVisited.add((i, j))

            if grid[i][j] == "1":
                findIsland(i+1, j)
                findIsland(i-1, j)
                findIsland(i, j+1)
                findIsland(i, j-1)
                return 1
            else:
                return 0
            
        for i in range(numRow):
            for j in range(numCol):
                res += findIsland(i, j)
                    
            
        return res
