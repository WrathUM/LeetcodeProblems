class Solution:
    def minimumPushes(self, word: str) -> int:
        frequencies = {k: v for k, v in sorted(Counter(word).items(), key = lambda item: -item[1])}
        
        res = 0
        count = 0
        tier = 0
        for k, v in frequencies.items():
            if count % 8 == 0:
                tier += 1

            res += tier * v
            count += 1
    
        return res
