def modifyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        options = [chr(i + ord('a')) for i in range(26)]
        res = ['0'] * len(s)
        for i in range(len(s)):
            prev = '-'
            nxt = '-'
            if s[i] == '?':
                if i - 1 >= 0:
                    prev = res[i - 1]
                if i + 1 < len(s):
                    nxt = s[i + 1]
                
                for letter in options:
                    if letter == prev or letter == nxt:
                        continue
                    res[i] = letter
                    break
            else:
                res[i] = s[i]
        return ''.join(res)
