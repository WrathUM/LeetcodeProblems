class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n = len(word)
        num_overlap = 0
        for i in range(k, n, k):
            print(word[0:n - i], word[i:])
            if word[0:n - i] == word[i:]:
                num_overlap = len(word[i:])
                break
        
        print(num_overlap)
        
        if num_overlap == 0:
            return math.ceil(len(word) / k)
        
        return math.ceil((n - num_overlap) / k)
