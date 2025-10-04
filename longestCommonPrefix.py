class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        tries = {}
        def populate(n):
            num = str(n)
            
            p = tries
            
            for c in num:
                if c in p:
                    p = p[c]
                else:
                    p[c] = {}
                    p = p[c]
            p['#'] = '#'
                    
        def traverse(n):
            num = str(n)
            res = 0
            p = tries
            for c in num:
                if c in p:
                    p = p[c]
                    res += 1
                else:
                    return res
            return res
        
        for num in arr1:
            populate(num)
        
        res = 0
        for num in arr2:
            res = max(res, traverse(num))
            
        return res
            
        # {1: {0: {0:}}}
        
        
