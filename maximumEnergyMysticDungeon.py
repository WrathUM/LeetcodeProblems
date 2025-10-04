class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        res = [0] * n
        for i in range(k):
            res[n - 1 - i] = energy[n - 1 - i]

        for i in range(n - k - 1, -1, -1):
            res[i] = energy[i] + res[i + k]
        return max(res)
