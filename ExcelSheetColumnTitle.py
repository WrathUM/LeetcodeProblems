def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        res = []
        
        n = len(str(columnNumber))
        val = columnNumber
        while val != 0:
            num = (val-1) % 26
            letter = chr(ord('A') + num)
            res.append(letter)
            val = (val-1) // 26
            print(letter)
        
        res = reversed(res)
        
        return ''.join(res)
        """
        BBB -> 2 * 26^2 + 2*26^1 + 2 * 26^0
        703 = AAA
        703 % 26 -> 1 
        
        3 % 2 == 1 
        1 % 2 == 0
        11
        
        
