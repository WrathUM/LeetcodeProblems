def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        n = len(arr)
        num_remove =  n / 20
        print(n)
        array_sorted = sorted(arr)
        print(array_sorted)
        
        subset = array_sorted[num_remove:(n-num_remove)]
        
        print(subset)
        
        return float(sum(subset))/(len(subset))
