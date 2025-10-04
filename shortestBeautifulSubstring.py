def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        i, j = 0, 0
        n = len(s)
        
        def compare(primary, alt):
            if primary == "":
                return alt
            
            if len(primary) > len(alt):
                return alt
            elif len(primary) < len(alt):
                return primary
            else:
                for i in range(len(alt)):
                    if  int(primary[i]) > int(alt[i]):
                        return alt
                    elif int(primary[i]) < int(alt[i]):
                        return primary
                return primary
        
        
        numOnes = int(s[0])
        if s[0] == "1" and k == 1:
            return "1"
        
        bestSoFar = ""
        while j < n:
            if numOnes >= k:
                # print("move left pointer")
                if int(s[i]) == 1:
                    numOnes -= 1
                
                i += 1
                
            else:
                # print("move right pointer")
                j += 1
                if j >= n:
                    break
                    
                if int(s[j]) == 1:
                    numOnes += 1
            
            # print(s[i: j + 1], numOnes)
            if numOnes == k:    
                bestSoFar = compare(bestSoFar, s[i: j + 1])
                
        
        
            
        return bestSoFar
