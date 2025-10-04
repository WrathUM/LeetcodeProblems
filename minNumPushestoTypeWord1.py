class Solution:
    def minimumPushes(self, word: str) -> int:
        mappings = defaultdict(int)
        count = 0
        tier = 0
        for i, c in enumerate(word):
            if c not in mappings:
                if i % 8 == 0:
                    tier += 1
                mappings[c] = tier
            count += mappings[c]
        
        return count
                
