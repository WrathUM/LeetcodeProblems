class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        n = len(s)
        len_a = len(a)
        len_b = len(b)
        
        a_starts = []
        b_starts = []
        
        for i in range(n):
            if s[i] == a[0] and "".join(s[i: i + len_a]) == a:
                a_starts.append(i)
        
        
        for i in range(n):
            if s[i] == b[0] and "".join(s[i: i + len_b]) == b:
                b_starts.append(i)
        
        res = []
        for v in a_starts:
            for c in b_starts:
                if abs(c - v) <= k and v not in res:
                    res.append(v)
                    break

        return sorted(res)
                
        
