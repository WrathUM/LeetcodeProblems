class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        n = len(word)
        if n == k:
            return 0
        
        substrings = [word[i:i+k] for i in range(0, n, k)]
        sf = Counter(substrings)
        s_sf = sorted(sf.items(), key=lambda item: -item[1])
        freq = s_sf[0][1]
        # print(substrings, sf, s_sf)
        return sum(sf.values()) - freq
