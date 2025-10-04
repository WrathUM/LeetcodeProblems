class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        middle = n // 2
        nums.sort()
        res = 0

        res += abs(nums[middle] - k)
        for i in range(n):
            if i < middle:
                res += max(0, nums[i] - k)
            elif i > middle:
                res += max(0, k - nums[i])
        return res
