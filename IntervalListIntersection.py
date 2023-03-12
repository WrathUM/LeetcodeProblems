def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        fLen = len(firstList)
        sLen = len(secondList)
        
        i = 0
        j = 0
        
        res = []
        
        while i < fLen and j < sLen:
            start1 = firstList[i][0]
            end1 = firstList[i][1]
            start2 = secondList[j][0]
            end2 = secondList[j][1]
            if start1 > end2 or start2 > end1:
                if start1 > start2:
                    j += 1
                else:
                    i += 1
                continue
            else:
                if end1 < end2:
                    res.append([max(start1, start2), end1])
                    i += 1
                elif end1 > end2:
                    res.append([max(start1, start2), end2])
                    j += 1
                else:
                    res.append([max(start1, start2), end1])
                    i += 1
                    j += 1
                    
                
        return res
