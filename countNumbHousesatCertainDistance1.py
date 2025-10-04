class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        def get_neighbors(i):
            neighbors = []
            if i <= 0 or i > n:
                return neighbors
            
            if i == x:
                neighbors.append(y)
            if i == y:
                neighbors.append(x)
            if i > 1:
                neighbors += [i - 1]
            if i < n: 
                neighbors += [i + 1]
            
            return neighbors
                
        res = [0] * (n + 1)

        
        
        for house in range(n + 1):
            visited = set()
            queue = [house]
            i = 0
            while queue:
                # print(queue)
                temp = []

                valid_children = 0
                for child in queue:
                    if child in visited:
                        continue
                    valid_children += 1
                    visited.add(child)
                    neighbor = get_neighbors(child)
                    temp += neighbor

                res[i] += valid_children

                queue = temp
                i += 1
        
        return res[1:]

    
        """
        1: 2,3
        
        """
