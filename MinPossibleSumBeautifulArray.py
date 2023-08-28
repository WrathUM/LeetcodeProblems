class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        if n == 1:
            return 1
        
        res = []
        
        val = 1
        while len(res) < n:
            diff = target - val
            if diff not in res:
                res.append(val)
            val += 1
        return sum(res)
            
