class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        num_occ = defaultdict(int)
        l, r = 0, 1
        num_occ[s[0]] += 1
        n = len(s)
        res = 0
        while r < n:
            num_occ[s[r]] += 1
            print(l, r)
            while num_occ[s[r]] > 2:
                num_occ[s[l]] -= 1
                l += 1
            
            r += 1
            res = max(res, r - l)

        return res
        
