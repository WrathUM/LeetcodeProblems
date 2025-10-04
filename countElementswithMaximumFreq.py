class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        
        num_copies = 0
        max_freq = 0
        for k, v in freq.items():
            if v > max_freq:
                num_copies = v
                max_freq = v
                continue
            if v == max_freq:
                num_copies += v
            
        return num_copies
