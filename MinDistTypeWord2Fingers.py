"""
Top Down Approach
The commented out code is how to use my own memo, over @cache
"""
def minimumDistance(self, word: str) -> int:
        def computeDistance(letter1, letter2):
            dist1 = ord(letter1) - ord('A')
            dist2 = ord(letter2) - ord('A')
            
            x1 = dist1 // 6
            y1 = dist1 % 6
            x2 = dist2 // 6
            y2 = dist2 % 6
            
            return (abs(x1-x2) + abs(y1-y2))
        
        
        #memo = [[-1] * len(word) for _ in range(len(word))]
        @cache
        def recurse(finger1, finger2):
            #if memo[finger1][finger2] != -1:
                #return memo[finger1][finger2]
            idx = max(finger1, finger2) + 1
            if len(word) == idx:
                return 0
 
            if finger1 == -1:
                path1 = recurse(idx, finger2)
            else:
                path1 = recurse(idx, finger2) + computeDistance(word[finger1], word[idx])

            if finger2 == -1:
                path2 = recurse(finger1, idx)
            else:
                path2 = recurse(finger1, idx) + computeDistance(word[finger2], word[idx])

            #memo[finger1][finger2] = min(path1, path2)
            #return memo[finger1][finger2]
            return min(path1, path2)
        
        res = min(recurse(0, -1), recurse(-1, 0))
        
        return res
