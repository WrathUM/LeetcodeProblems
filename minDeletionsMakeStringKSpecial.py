class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = Counter(word)
        
        res = float('inf')
        running_sum = 0
        
        vals = sorted(freq.values())
        
        for i in range(len(vals)):
            smallest = vals[i]
            
            local_best = running_sum
            for j in range(i + 1, len(vals)):
                count = vals[j]
                if count > (smallest + k):
                    local_best += (count - (smallest + k))
            
            res = min(res, local_best)
            
            running_sum += smallest
            
                
        return res
            
            
    
        """
        a: 1    [0,1,2,4]
        b: 2    [1,0,1,3]
        c: 3    [2,1,0,2]
        d: 5    [4,3,2,0]
        
        k: 2
        
        
        """
        
        
