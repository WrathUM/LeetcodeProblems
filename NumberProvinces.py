"""
Speed: 
Space:
"""
def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        visited = set()
        
        n = len(isConnected)
        res = 0
        bfs = deque()
        for i in range(n):
            if i in visited:
                continue
            bfs.append(i)
            while len(bfs) != 0:
                j = bfs.popleft()
                for k in range(n):
                    if k in visited:
                        continue
                    if isConnected[j][k] == 1:
                        bfs.append(k)
                        visited.add(k)
            res += 1
                
        return res
