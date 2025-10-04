class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        i = 0
        n = len(nums)
        hash_map = defaultdict(int)
        c = []
        heapify(c)
        ans = [0] * n
        
        while i < n:
            hash_map[nums[i]] += freq[i]
            heapq.heappush(c, (-hash_map[nums[i]], nums[i]))
            f, id = c[0]
            while -f != hash_map[id]:
                heapq.heappop(c)
                f, id = c[0]

            ans[i] = -f
            i += 1
        
        return ans

