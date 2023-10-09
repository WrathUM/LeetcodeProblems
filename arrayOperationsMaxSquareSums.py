class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        buckets = [0] * 32
        for v in nums:
            for i in range(33):
                if v & (1 << i) == (1 << i):
                    buckets[i] += 1
        
        fNums = [0] * k
        
        for i in range(k):
            for j, b in enumerate(buckets):
                if b > 0:
                    fNums[i] += 1 << j
                    buckets[j] -= 1
        

        res = 0
        for v in fNums:
            res += v**2
        
        return res % (10**9 + 7)
