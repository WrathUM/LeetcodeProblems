def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxJump = nums[0]
        i = 0 
        
        while i <= maxJump:
            if nums[i] != 0:
                maxJump = max(maxJump, i + nums[i])
            if maxJump >= (len(nums) - 1):
                return True
            i += 1
        
        if maxJump >= (len(nums) - 1):
            return True
        return False
