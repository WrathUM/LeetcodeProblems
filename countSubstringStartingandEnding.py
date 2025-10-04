class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        positions = []
        for i, w in enumerate(s):
            if w == c:
                positions.append(i)
            
        
        n = len(positions)
        res = 0
        for i in range(n):
            res += i + 1
            
        return res
