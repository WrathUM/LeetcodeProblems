def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        width = len(matrix[0])
        height = len(matrix)
        
        visited = set()
        n = width * height
        
        
        res = []
        i,j = 0,0
        r,l,u,d = True, False, False, False
        while len(visited) != n:
            print((j,i))
            visited.add((j,i))
            res.append(matrix[j][i])

            if u:
                if j - 1 >= 0 and (j - 1, i) not in visited:
                    j -= 1
                    continue
                else:
                    i += 1
                    r = True
                    u = False
                    continue
                
            elif l:
                if i - 1 >= 0 and (j, i - 1) not in visited:
                    i -= 1
                    continue
                else:
                    j -= 1
                    u = True
                    l = False
                    continue
                
            elif r: 
                if i + 1 < width and (j,i + 1) not in visited:
                    i += 1
                    continue
                else:
                    j += 1
                    d = True
                    r = False
                    continue
                
            elif d: 
                if j + 1 < height and (j + 1, i) not in visited:
                    j += 1
                    continue
                else:
                    i -= 1
                    l = True
                    d = False
                    continue

        return res
