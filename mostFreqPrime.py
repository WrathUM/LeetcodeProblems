class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        counts = defaultdict(int)
        m = len(mat)
        n = len(mat[0])
        
        def dfs(value, x, y, d_x, d_y):
            if x >= m or x < 0 or y >= n or y < 0:
                return 
            
            value = value * 10 + mat[x][y]

            counts[value] += 1
            dfs(value, x + d_x, y + d_y, d_x, d_y)
            
        for i in range(m):
            for j in range(n):
                val = mat[i][j]
                for w in range(-1, 2):
                    for z in range(-1, 2):
                        if w != 0 or z != 0:
                            dfs(0, i, j, w, z)
                
        items = sorted(counts.items(), key=lambda x: -x[1])
        
        def isPrime(n):
            for i in range(2, int(sqrt(n)) + 1):
                if (n % i == 0):
                    return False
            return True
        
        print(items)
        
        best = -1
        best_freq = 0
        for i, j in items:
            if i > 10 and isPrime(i):
                
                if j >= best_freq and i > best:
                    best = i
                    best_freq = j
                # print(i,j, best, best_freq)
            
        return best
        
