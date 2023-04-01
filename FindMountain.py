# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        n = mountain_arr.length()
        # find index of peak
        l, r = 0, n - 1
        while l < r:
            m = (l + r) / 2
            if mountain_arr.get(m) < mountain_arr.get(m + 1):
                l = peak = m + 1
            else:
                r = m
        # find target in the left of peak
        l, r = 0, peak
        while l <= r:
            m = (l + r) / 2
            if mountain_arr.get(m) < target:
                l = m + 1
            elif mountain_arr.get(m) > target:
                r = m - 1
            else:
                return m
        # find target in the right of peak
        l, r = peak, n - 1
        while l <= r:
            m = (l + r) / 2
            if mountain_arr.get(m) > target:
                l = m + 1
            elif mountain_arr.get(m) < target:
                r = m - 1
            else:
                return m
        return -1
