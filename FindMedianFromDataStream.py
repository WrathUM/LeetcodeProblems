class MedianFinder(object):

    def __init__(self):
        self.values = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        idx = bisect.bisect(self.values, num)
        self.values.insert(idx, num)

    def findMedian(self):
        """
        :rtype: float
        """
        n = len(self.values)
        if n % 2 == 0:
            v1 = self.values[n//2]
            v2 = self.values[n//2 - 1]

            return ((v1 + v2) / 2.0)
        else:
            return self.values[n//2]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
