"""
Speed: 77.82 Percentile
Space: 6.61 Percentile
"""
def reverseStr(self, s, k):
      """
      :type s: str
      :type k: int
      :rtype: str
      """
      vec = [s[start:start+k] for start in range(0, len(s), k)]

      for i in range(len(vec)):
          if i % 2 == 0:
              vec[i] = "".join(reversed(vec[i]))

      return "".join(vec)
