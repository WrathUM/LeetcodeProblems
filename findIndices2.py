class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        mins = [0] * n
        maxs = [0] * n
        
        
        for i in range(0, n):
            if nums[i] < nums[mins[i - 1]]:
                mins[i] = i
            else:
                mins[i] = mins[i-1]
            
            if nums[i] > nums[maxs[i - 1]]:
                maxs[i] = i
            else:
                maxs[i] = maxs[i-1]
              
        print(mins, maxs)    
        
        j = indexDifference
        while j < n:
            mVal = abs(nums[j] - nums[mins[j - indexDifference]])
            val = abs(nums[j] - nums[maxs[j-indexDifference]])
            
            if mVal >= valueDifference:
                return [mins[j - indexDifference], j]
            elif val >= valueDifference:
                return [maxs[j - indexDifference], j]
            
            j += 1
        
        return [-1, -1]
            
        
        """
        [1,2,3,4,5]
        [1,1,1,1,1]
        [1,2,3,4,5]
        2
        4
        j = 2
        """
