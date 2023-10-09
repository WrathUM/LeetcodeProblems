class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        pTime = sorted(processorTime)
        tTime = sorted(tasks)
        
        best = 0
        idx = len(tTime) - 1
        for p in pTime:
            if p + tTime[idx] > best:
                best = p + tTime[idx]
            idx -= 4
            
        return best
