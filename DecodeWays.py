def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        memo = [0] * len(s)
        
        valid = [str(i) for i in range(1,27)]
        def recurse(val):
            # base case
            if len(val) == 0 or val == "":
                return 1 
            if memo[len(val) - 1] != 0:
                return memo[len(val) - 1]
            
            m,n = 0,0
            for v in valid:
                if m != 0 and n != 0:
                    break
                if val.startswith(v):
                    if len(v) == 1:
                        m += recurse(val[1:])
                    else:
                        n += recurse(val[2:])
            
            memo[len(val) - 1] = m + n
            return m + n
    
        res = recurse(s)
        
        return res
