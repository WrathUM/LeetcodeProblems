class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        def isPrefixSuffix(a, b) -> bool:
            n = len(a)
            m = len(b)
            if n > m:
                return False
            
            for i in range(n):
                front, back = a[i], a[n-i-1]
                if front != b[i] or back != b[m-i-1]:
                    return False
            
            return True
        
        res = 0
        
        for i in range(len(words)):
            for j in range(len(words)):
                if i >= j:
                    continue
                v = isPrefixSuffix(words[i], words[j])
                if v:
                    res += 1
                    
        return res
