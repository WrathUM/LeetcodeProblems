"""
Alternative Write up uses:
for dx, dy in [(i+1, j), (i, j+1), ...]:
  Check
  Add to Visited
  Recurse
  Remove from Visited
  Replaces lines 18-43
"""

def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        nValid = 0
        nrow = len(grid)
        ncol = len(grid[0])
        res = 0
        
        def dfs(i, j, visited, res):
            if grid[i][j] == -1:
                return res
            if grid[i][j] == 2 and len(visited) == nValid:
                res += 1
                return res
            
            if [i + 1, j] not in visited and i + 1 < nrow:
                visited.append([i + 1, j])
                res = dfs(i + 1, j, visited, res)
                visited.pop()
            if [i, j + 1] not in visited and j + 1 < ncol:
                visited.append([i, j + 1])
                res = dfs(i, j + 1, visited, res)
                visited.pop()
            if [i - 1, j] not in visited and i - 1 >= 0:
                visited.append([i - 1, j])
                res = dfs(i - 1, j, visited, res)
                visited.pop()
            if [i, j - 1] not in visited and j - 1 >= 0:
                visited.append([i, j - 1])
                res = dfs(i, j - 1, visited, res)
                visited.pop()
            
            return res
            
        
        start = [-1,-1]
        visited = []
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] != -1:
                    nValid += 1
                if grid[i][j] == 1:
                    start[0] = i
                    start[1] = j
        
        visited.append(start)
        res = dfs(start[0], start[1], visited, res)
        
        return res
