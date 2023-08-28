class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        if sum(nums) < target:
            return -1
        
        if target in nums:
            return 0
        
        # sort
        count = [0] * 31
        for v in nums:
            count[int(math.log(v, 2))] += 1
            
        # start from 1 and look for items
        steps = 0
        for i, c in enumerate(count):
            # print(count)
            if target == 0:
                return steps
            mask = 1 << i
            # print(target, mask, target & mask)
            if target & mask == mask:
                # print(i, c)
                if c > 0:
                    target -= mask
                    count[i] -= 1
                else:
                    j = i
                    while count[i] == 0:
                        if count[j] == 0:
                            j += 1
                        else:
                            steps += 1
                            count[j] -= 1
                            count[j - 1] += 2
                            j -= 1
                            
                    target -= mask
                    count[i] -= 1
            # consolidate
            pairs = count[i] // 2
            if i + 1 <= 30:
                count[i + 1] += pairs  

        return steps
