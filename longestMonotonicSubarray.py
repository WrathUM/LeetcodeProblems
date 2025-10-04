class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        diffs = [0] * (n-1)
        
        for i in range(n - 1):
            v = nums[i+1] - nums[i]
            if v > 0:
                diffs[i] = 1
            elif v < 0:
                diffs[i] = -1
            else:
                diffs[i] = 0
        
        value = None
        cur = 0
        res = 1
        for i in range(n - 1):
            if diffs[i] == 0:
                cur = 1
                continue
            if value is None:
                value = diffs[i]
                cur = 2
                res = max(cur, res)
                continue
            if diffs[i] == value:
                cur += 1
                res = max(cur, res)
            else:
                value = diffs[i]
                cur = 2
        
        return res
            
