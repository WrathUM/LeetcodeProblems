"""
In place will use a 2 pointer based solution.
"""

def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0] * len(nums)
        
        odd = 1
        even = 0
        
        for num in nums:
            if num % 2 == 0:
                res[even] = num
                even += 2
            else:
                res[odd] = num
                odd += 2
        return res
