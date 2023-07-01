def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        if num2 > num1:
            return -1
        
        def numOnes(n):
            res = 0
            while n > 0:
                if n & 1:
                    res += 1
                n = n >> 1
            return res
        
        output = 0
        cur = num1
        while True:
            temp = cur - output * num2
            if output > temp:
                break
            if temp <= 0:
                break
            if numOnes(temp) <= output:
                return output
            else:
                output += 1
            
        return -1
