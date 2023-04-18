def frequencySort(self, s: str) -> str:
        characters = set()
        counts = defaultdict(int)
        
        for i in range(len(s)):
            if s[i] not in characters:
                characters.add(s[i])
            counts[s[i]] += 1
            
        res = ""
        v = sorted(counts.items(), key=lambda x:-x[1])
        for c,k in v:
            for i in range(k):
                res += c
        
        return res
