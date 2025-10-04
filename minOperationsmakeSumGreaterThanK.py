class Solution:
    def minOperations(self, k: int) -> int:
        i = 1.0
        res = float(10**5+1)
        while i <= k:
            num_times = ceil(k / i)
            res = min(res, num_times - 1 + i - 1)
            i += 1

        return int(res)
