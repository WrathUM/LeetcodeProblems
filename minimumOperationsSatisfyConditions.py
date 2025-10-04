class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        numRows = len(grid)
        numCols = len(grid[0])
        col_assigments = [-1] * numCols
        col_freqs = [[0]] * numCols

        def freq_counts(n, col):
            buckets = [0] * 10
            for i in range(n):
                buckets[grid[i][col]] += 1
            return buckets

        @cache
        def recurse(cur_col, prev_col_val):
            if cur_col >= numCols:
                return 0
            lowest_cost = float('inf')
            for i in range(10):
                if i != prev_col_val:
                    cost = numRows - col_freqs[cur_col][i]
                    cost += recurse(cur_col + 1, i)
                    lowest_cost = min(lowest_cost, cost)

            return lowest_cost

        for i in range(numCols):
            col_freqs[i] = freq_counts(numRows, i)

        return recurse(0, -1)
            

        

        





        
