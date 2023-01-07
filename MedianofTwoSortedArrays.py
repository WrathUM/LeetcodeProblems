class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1_size = len(nums1)
        l2_size = len(nums2)
        
        idx1, idx2 = 0, 0
        _idx1, _idx2 = False, False
        first_val = 0
        sec_val = 0
        
        mid_idx = (l1_size + l2_size) // 2 + 1
        
        while (idx1 + idx2 < mid_idx):
            if (idx1 == l1_size):
                _idx1 = True
                break
            elif (idx2 == l2_size):
                _idx2 = True
                break
                
            if nums1[idx1] <= nums2[idx2]:
                first_val = sec_val
                sec_val = nums1[idx1]
                idx1 += 1
            else:
                first_val = sec_val
                sec_val = nums2[idx2]
                idx2 += 1
        
        # one of the lists reaches the end first
        if _idx1:
            while (idx1 + idx2 < mid_idx):
                first_val = sec_val
                sec_val = nums2[idx2]
                idx2 += 1
        elif _idx2:
            while (idx1 + idx2 < mid_idx):
                first_val = sec_val
                sec_val = nums1[idx1]
                idx1 += 1
            
        if (l1_size + l2_size) % 2 == 0:
            return float(first_val + sec_val)/2
        else:
            return sec_val
            
