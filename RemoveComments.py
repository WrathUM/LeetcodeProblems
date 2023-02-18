def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        res = []
        blockQuote = False
        closing = False
        for line in source:
            opening = False
            closing = False
            code = []
            if blockQuote and line.find('*/') == -1:
                continue
            i = 0
            while i < len(line):
                if blockQuote:
                    if line[i] == '*' and line[i+1] == '/':
                        i += 2
                        blockQuote = False
                        closing = True
                        continue
                    else:
                        i += 1
                        continue
                
                if i+1  < len(line) and line[i] == '/' and line[i+1] == '/':
                    break
                elif i+1  < len(line) and line[i] == '/' and line[i+1] == '*':
                    i += 2
                    blockQuote = True
                    opening = True
                    continue
            
                code.append(line[i])
                i += 1
            if code != []:
                if closing and not opening:
                    res[-1] += ("".join(code))
                    continue
                res.append("".join(code))
            
            
        return res
