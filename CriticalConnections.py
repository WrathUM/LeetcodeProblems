# Algorithm on https://en.wikipedia.org/wiki/Bridge_(graph_theory)#Tarjan%27s_bridge-finding_algorithm
"""
Speed: 68.18 Percentile
Space: 72.73 Percentile
"""
class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        visited = [0] * n
        tin = [-1] * n
        low = [-1] * n
        res = []
        self.time = 0
        
        def dfs(node, parent):
            low[node] = tin[node] = self.time
            self.time += 1
            visited[node] = 1    
            for child in graph[node]:
                if child == parent:
                    continue         
                if visited[child] != 1:
                    dfs(child, node)
                    
                    low[node] = min(low[node], low[child])
                    
                    if tin[node] < low[child]:
                        res.append([child, node]) 
                else:
                    low[node] = min(low[node], tin[child])
            
        graph = [[] for _ in range(n)]
        for v1, v2 in connections:
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        dfs(0, -1)
        return res
