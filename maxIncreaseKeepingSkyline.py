def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        nrows = len(grid)
        ncols = len(grid[0])
        
        grid2 = [[0] * ncols for _ in range(nrows)]

        for i in range(nrows):
            for j in range(ncols):
                rowMax = max(grid[i])

                colMax = 0
                colVals = []
                for k in range(nrows):
                    colVals.append(grid[k][j])
                colMax = max(colVals)


                val = min(rowMax, colMax)

                grid2[i][j] = val
                res += (val - grid[i][j])

        return res
