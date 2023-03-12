def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        isPositive = []
        for i in range(1,len(nums)):
            diff = nums[i] - nums[i-1]
            if diff > 0:
                isPositive.append(True)
            elif diff < 0:
                isPositive.append(False)
            else:
                continue
                
        for i in range(len(isPositive) - 1):
            if isPositive[i] != isPositive[i+1]:
                return False
            
        return True
