class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        def distance(s1, s2):
            v1, v2 = ord(s1) - ord('a'), ord(s2) - ord('a')
            if v1 != v2:
                dist = min(abs(v2 - v1), abs(v2 - v1 + 26))
                return dist
            return 0
            
        n = len(s)
        ordinal_values = [ord(x) for x in s]
        res = ['a'] * n
        budget = 0
        i = 0
        while budget < k and i < n:
            cost = distance(s[i], res[i])
            if budget + cost <= k:
                budget += cost
            else:
                val = ord(s[i]) - (k - budget)
                res[i] = chr(val)
                budget = k
            i += 1
        while i < n:
            res[i] = s[i]
            i += 1
        
        return "".join(res)
