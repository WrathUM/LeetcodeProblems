class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        diffs = defaultdict(int)
        for i in range(n):
            for j in range(m):
                diffs[nums2[j] - nums1[i]] += 1
        
        def validate(diff):
            #print(Counter(nums1))
            #print(Counter([x-diff for x in nums2]))
            return all(item[0] in Counter(nums1) and Counter(nums1)[item[0]] >= item[1] for item in Counter([x-diff for x in nums2]).items())
            #return all(nums1.count(v) == nums2.count(v + diff) for v in set(nums1))
            #return Counter([x-diff for x in nums2]).value() <= Counter(nums1).value()
            # value_freq = Counter(nums1)
            # for v in nums2:
            #     if v + diff in value_freq and value_freq[v+diff] != 0:
            #         value_freq[v+diff] -= 1


        res = sorted(diffs.items(), key=lambda x: x[0])
        #print(res)
        for x in range(-1000, 1001):
            if validate(x):
                return x


            
            
