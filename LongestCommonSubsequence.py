"""
Speed: 45.52 percentile
Space: 72.53 percentile
"""
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        numCols = len(text2)
        numRows = len(text1)

        memo = [[0] * numCols for _ in range(numRows)]

        memo[0][0] = 1 if text1[0] == text2[0] else 0
        for i in range(1, numCols):
            memo[0][i] = max(memo[0][i-1], 1 if text1[0] == text2[i] else 0)

        for i in range(1, numRows):
            memo[i][0] = max(memo[i-1][0], 1 if text1[i] == text2[0] else 0)

        for i in range(1, numRows):
            for j in range(1, numCols):
                memo[i][j] = max(memo[i-1][j], memo[i][j-1], memo[i-1][j-1] + 1 if text1[i] == text2[j] else 0)

        return memo[numRows - 1][numCols - 1]
