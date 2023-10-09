class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        n = len(s1)
        wIndex = []
        for i in range(n):
            if s1[i] != s2[i]:
                wIndex.append(i)

        if len(wIndex) % 2 != 0:
            return -1
        
        # two pointer
        p1, p2 = 0, len(wIndex) - 1
        
        memo = defaultdict(int)
        
        # [2, 600, 601, 1000]
        
        def recurse(p1, p2):
            if (p1, p2) in memo:
                return memo[(p1, p2)]
            
            if p1 > p2:
                return 0
            
            cost = float('inf')
            # match with neighbor [2, 600]
            cost = min(cost, recurse(p1 + 2, p2) + min(wIndex[p1 + 1] - wIndex[p1], x))
            # match end neighbors [601, 1000]
            cost = min(cost, recurse(p1, p2 - 2) + min(wIndex[p2] - wIndex[p2 - 1], x))
            # match with end [2, 1000]
            cost = min(cost, recurse(p1 + 1, p2 - 1) + min(wIndex[p2] - wIndex[p1], x))
            
            memo[(p1, p2)] = cost
            
            return cost
        
        return recurse(0, len(wIndex) - 1)
