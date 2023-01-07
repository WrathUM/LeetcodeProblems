"""
Speed: 92.60 percentile
Space: 48.92 percentile
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        idxDict = {}
        for i in range(len(nums)):
            if nums[i] in idxDict: # if its pair is found, then we have a pair
                return [idxDict[nums[i]], i] 
            idxDict[target - nums[i]] = i # Place the corresponding pair into the dict
"""
Intuition:
xa = target - xb

Thus if nums[i] == xa and xa in dictionary, then we must have found an xb prior. 
Since only one solution exists, this must be the final answer
"""
