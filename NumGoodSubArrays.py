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
#         count = 0
#         foundOne = False
        
#         for n in nums:
#             if n == 1:
#                 foundOne = True
#                 if res == 0:
#                     res = 1
#                     continue
#                 res *= (count + 1)
#                 count = 0
            
#             if foundOne:
#                 count += 1
        
        
        
        return res % (10**9 + 7)
