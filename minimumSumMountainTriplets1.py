class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = [0] * n, [0] * n
        left[0] = 0
        for i in range(1, n):
            if nums[left[i-1]] < nums[i]:
                left[i] = left[i-1]
            else:
                left[i] = i
        
        right[-1] = n - 1
        for i in range(n - 2, 0, -1):
            if nums[right[i + 1]] < nums[i]:
                right[i] = right[i + 1]
            else:
                right[i] = i
            
        print(left, right)
        
        def isMountain(vI, vJ, vK):
            if vI < vJ and vJ > vK:
                return vI + vJ + vK
            return float('inf')
        
        smallest = float('inf')
        
        for i in range(1, n - 1):
            
            val = isMountain(nums[left[i]], nums[i], nums[right[i]])
            smallest = min(smallest, val)
        
        if smallest < float('inf'):
            return smallest
        
        return -1
