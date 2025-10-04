class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        moves = 0
        
        sA = list(s)
        
        if n == 1:
            return 0
        
        # all ones right
        p1 = 0
        p2 = 1
        
        while p2 < n:
            if sA[p1] == '0':
                p1 += 1
                p2 += 1
            else:
                if sA[p2] == '0':
                    moves += p2 - p1
                    sA[p2] = '1'
                    sA[p1] = '0'
                    p1 += 1
                    p2 += 1
                else:
                    p2 += 1
        
        return moves
        
        
        """
        101
        p1 = 0
        p2 = 1
        
        011
        p1 = 1
        p2 = 3
        """
