class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        for i in range(n - indexDifference):
            for j in range(i + indexDifference, n):
                # print(i, j)
                vDiff = abs(nums[i] - nums[j])
                # print(vDiff)
                if vDiff >= valueDifference:
                    return [i, j]
        
        return [-1, -1]
            
        
            
            
