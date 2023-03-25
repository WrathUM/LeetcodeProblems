def numTimesAllBlue(self, flips):
        """
        :type flips: List[int]
        :rtype: int
        """
        bString = [0] * len(flips)
        res = 0
        
        def checkPrefixAligned(bString, idx):
            for i in range(idx + 1):
                if bString[i] == 0:
                    return False
            
            return True
        
        largest = 0
        for i in range(len(flips)):
            largest = max(flips[i] - 1, largest)
            if largest == i:
                res += 1
            # bString[flips[i] - 1] = 1
            # if checkPrefixAligned(bString, i):
            #     res += 1
        
        return res
