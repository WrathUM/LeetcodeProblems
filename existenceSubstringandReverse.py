class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        r = s[::-1]
        n = len(s)
        substrings = set()
        for i in range(n - 1):
            w = s[i:i+2]
            substrings.add(w)
            
        for i in range(n - 1):
            w = r[i:i+2]
            if w in substrings:
                return True
            
        return False
