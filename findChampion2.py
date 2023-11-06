class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        numIn = defaultdict(int)
        
        for src, dst in edges:
            numIn[dst] += 1
        
        smallest = float('inf')
        small_idx = -1
        for i in range(n):
            v = numIn[i]
            if v < smallest:
                smallest = v
                small_idx = i
            elif v == smallest:
                small_idx = -1
                
        return small_idx
