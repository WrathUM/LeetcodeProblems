def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        val1 = set(nums1)
        val2 = set()
        seen2 = set()

        for v in nums2:
            if v in seen2:
                continue
            else:
                seen2.add(v)
            if v in val1:
                val1.remove(v)
            else:
                val2.add(v)

        
        return [list(val1), list(val2)]
