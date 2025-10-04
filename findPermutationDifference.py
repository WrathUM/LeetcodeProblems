class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        n = len(s)
        sC, tC = {}, {}

        for i in range(n):
            sC[s[i]] = i
            tC[t[i]] = i
        
        res = 0
        for k in sC.keys():
            v1 = sC[k]
            v2 = tC[k]
            res += abs(v2 - v1)

        return res
