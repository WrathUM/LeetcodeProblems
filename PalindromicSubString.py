def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        res = n
        for i in range(n):
            j = 1
            center = s[i]
            valid = True
            while valid:
                left = ''
                right = ''
                if i - j >= 0:
                    left = s[i - j]
                if i + j < n:
                    right = s[i + j]
                if right != '' and left != '' and right == left:
                    res += 1
                    j += 1
                else:
                    valid = False
                    
            if  i - 1 >= 0 and s[i - 1] == center:
                j = 0
                valid = True
                while valid:
                    left = ''
                    right = ''
                    if i - j - 1 >= 0:
                        left = s[i - j - 1]
                    if i + j < n:
                        right = s[i + j]
                    if right != '' and left != '' and right == left:
                        res += 1
                        j += 1
                    else:
                        valid = False
        
        return res
