def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        def dfs(cur):
            if cur not in self.graph or target not in self.graph:
                return -1
            if cur == self.goal:
                return 1
            
            if self.goal in self.graph[cur]:
                return self.graph[cur][self.goal]
            
            for node in self.graph[cur]:
                if node not in self.seen:
                    self.seen.add(node)
                    temp = dfs(node)
                    if temp == -1:
                        continue
                    else:
                        return temp * self.graph[cur][node]
            return -1
            
        
        self.graph = defaultdict(dict)
        self.seen = set()
        
        for pair, v in zip(equations, values):
            c1, c2 = pair
            self.graph[c1][c2] = v
            self.graph[c2][c1] = 1/v
                 
        res = []
        for origin, target in queries:
            self.goal = target
            res.append(dfs(origin))
            self.seen.clear()
            
        return res
