def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        
        # longest common subsequence
        numCols = len(str2)
        numRows = len(str1)
        memo = [[''] * numCols for _ in range(numRows)]
        
        memo[0][0] = str1[0] if str1[0] == str2[0] else ''
        for i in range(1, numCols):
            memo[0][i] = str1[0] if str1[0] == str2[i] else ''
            if len(memo[0][i-1]) >= len(memo[0][i]):
                memo[0][i] = memo[0][i-1]
                
        for i in range(1,numRows):
            memo[i][0] = str2[0] if str1[i] == str2[0] else ''
            if len(memo[i-1][0]) >= len(memo[i][0]):
                memo[i][0] = memo[i-1][0]
        
        for i in range(1,numRows):
            for j in range(1,numCols):
                memo[i][j] = max([memo[i-1][j], 
                                  memo[i][j-1],
                                  memo[i-1][j-1] + str1[i] if str1[i] == str2[j] else ''], 
                                 key = len)
                # subTop = memo[i-1][j]
                # subLeft = memo[i][j-1]
                # subAlt = memo[i-1][j-1] + str1[i] if str1[i] == str2[j] else ''
#                 if len(subLeft) > len(subTop) and len(subLeft) > len(subAlt):
#                     memo[i][j] = subLeft
#                 elif len(subAlt) > len(subTop) and len(subAlt) > len(subLeft):
#                     memo[i][j] = subAlt
#                 else:
#                     memo[i][j] = subTop
        
        subSeq = memo[numRows - 1][numCols-1]
        # print(memo)
        # print(subSeq)
        # each one is indexed back to its spots in str1 and str2
        res = ""
        idx1, idx2, idx3 = 0,0,0
        while (idx1 < numRows and idx2 < numCols and idx3 < len(subSeq)):
            # print(str1[idx1], str2[idx2], subSeq[idx3])
            if str1[idx1] == subSeq[idx3] and str2[idx2] == subSeq[idx3]:
                idx2 += 1
                idx1 += 1
                res += subSeq[idx3]
                idx3 += 1
            elif str1[idx1] == subSeq[idx3]:
                res += str2[idx2]
                idx2 += 1
            elif str2[idx2] == subSeq[idx3]:
                res += str1[idx1]
                idx1 += 1
            else:
                res += str1[idx1]
                idx1 += 1
                res += str2[idx2]
                idx2 += 1
                
        if idx2 < numCols:
            for i in range(idx2, numCols):
                res += str2[i]
            
        if idx1 < numRows:
            for i in range(idx1, numRows):
                res += str1[i]
        
        return res
