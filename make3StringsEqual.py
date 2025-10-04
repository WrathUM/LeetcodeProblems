class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        n = min(len(s1), len(s2), len(s3))
        sum_len = len(s1) + len(s2) + len(s3)
        i = 0
        if s1[i] != s2[i] or s1[i] != s3[i] or s2[i] != s3[i]:
            return -1
            
        for i in range(n):
            if s1[i] == s2[i] == s3[i]:
                sum_len -= 3
            else:
                break
                
        return sum_len
