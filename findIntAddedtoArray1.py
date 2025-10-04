class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = sorted(nums1), sorted(nums2)

        diff = n2[0] - n1[0]

        return diff
