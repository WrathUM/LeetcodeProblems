def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        res = 1
        
        nums = [str(x) for x in nums]
        
        s = "".join(nums)
        s = s.strip('0')
        l = s.split("1")
        
        if len(l) == 1:
            return 0
        
        for v in l:
            res *= (len(v) + 1)

        return res % (10**9 + 7)
