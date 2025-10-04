class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        position = 0
        res = 0
        for v in nums:
            position += v
            if position == 0:
                res += 1
                
        return res
                
