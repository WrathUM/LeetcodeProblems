class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        s1 = defaultdict(int)
        s2 = defaultdict(int)
        
        for v in nums1:
            s1[v] += 1
        for v in nums2:
            s2[v] += 1
        
        remove1 = 0
        remove2 = 0
        # print(s1, s2)
        while remove1 < n/2:
            for k, v in s1.items():
                if v > 1:
                    remove1 += v - 1
                    v = 1
                    
            if remove1 >= n/2:
                break
            for k, v in s1.items():
                if k in s2 and s2[k] != 0:
                    s1[k] = 0
                    remove1 += 1
                    if remove1 >= n/2:
                        break
            if remove1 >= n/2:
                break
            for k, v in s1.items():
                if s1[k] > 0:
                    s1[k] = 0
                    remove1 += 1
                    if remove1 >= n/2:
                        break
            
        while remove2 < n/2:
            for k, v in s2.items():
                if v > 1:
                    remove2 += v - 1
                    v = 1
            if remove2 >= n/2:
                break
            for k, v in s2.items():
                if k in s1 and s1[k] != 0:
                    s2[k] = 0
                    remove2 += 1
                    if remove2 >= n/2:
                        break
            if remove2 >= n/2:
                break
            for k, v in s2.items():
                if s2[k] > 0:
                    s2[k] = 0
                    remove2 += 1
                    if remove2 >= n/2:
                        break

        s = set()
        for k, v in s1.items():
            if v != 0: 
                s.add(k)
        for k, v in s2.items():
            if v != 0: 
                s.add(k)
       
        return len(s)
