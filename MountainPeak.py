def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        low, high = 0, len(arr) - 1
        while(low <= high):
            mid = (low + (high - low)//2)
            rightMid = arr[mid + 1]
            leftMid = arr[mid - 1]
            val = arr[mid]
            if rightMid < val and leftMid < val:
                return mid
            elif rightMid > val:
                low = mid + 1
            else:
                high = mid - 1
        return -1
