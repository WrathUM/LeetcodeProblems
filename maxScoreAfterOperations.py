class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        connections = defaultdict(list)
        
        for src, dst in edges:
            connections[src].append(dst)
            connections[dst].append(src)
        
        visited = set()
        @cache
        def recurse(root, isSkipped):
            v = values[root]
            children = connections[root]
            best1 = 0
            flag = False
            
            for c in children:
                if c not in visited:
                    flag = True
                    visited.add(c)
                    best1 += recurse(c, True)
                    visited.remove(c)
            
            best2 = v
            for c in children:
                if c not in visited:
                    flag = True
                    visited.add(c)
                    best2 += recurse(c, isSkipped)
                    visited.remove(c)
            
            if not flag and not isSkipped:
                best2 = 0

            return max(best1, best2)
        
        visited.add(0)
        return recurse(0, False)
        
        
