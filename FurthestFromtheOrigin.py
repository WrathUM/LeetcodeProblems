class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        numR, numL, num_ = 0,0,0
        
        for c in moves:
            if c == 'R':
                numR += 1
            elif c == 'L':
                numL += 1
            else:
                num_ += 1
                
        
        if numR > numL:
            return numR - numL + num_
        elif numR < numL:
            return numL - numR + num_
        else:
            return num_
        
        
    
