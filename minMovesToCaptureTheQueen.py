class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        # go outwards up left
        x, y = c - 1 , d - 1
        rookFound = False
        
        while x >= 1 and y >= 1:
            if x == a and y == b:
                rookFound = True
            if x == e and y == f:
                if rookFound:
                    return 2
                else:
                    return 1
            x -= 1
            y -= 1
        
        # down left
        x, y = c + 1 , d - 1
        rookFound = False
        while x <= 8 and y >= 1:
            if x == a and y == b:
                rookFound = True
            if x == e and y == f:
                if rookFound:
                    return 2
                else:
                    return 1
            x += 1
            y -= 1
            
            
        # up right    
        x, y = c - 1 , d + 1
        rookFound = False
        while x >= 1 and y <= 8:
            if x == a and y == b:
                rookFound = True
            if x == e and y == f:
                if rookFound:
                    return 2
                else:
                    return 1
            x -= 1
            y += 1
        
        # up right    
        x, y = c + 1 , d + 1
        rookFound = False
        while x <= 8 and y <= 8:
            if x == a and y == b:
                rookFound = True
            if x == e and y == f:
                if rookFound:
                    return 2
                else:
                    return 1
            x += 1
            y += 1
        
        if a == e or b == f:
            if a == e and a == c and (d - b) * (d - f) < 0:
                return 2
            if b == f and b == d and (c - a) * (c - e) < 0:
                return 2
            return 1
        
        return 2
