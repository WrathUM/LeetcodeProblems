def countBeautifulPairs(self, nums: List[int]) -> int:
        res = 0

        def gcd(a, b):
            if a == 0:
                return b
            
            return gcd(b % a, a)
        
        
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                a,b = int(str(nums[i])[0]), int(str(nums[j])[-1])
                if gcd(a,b) == 1:
                    res += 1
                    
        
        return res
