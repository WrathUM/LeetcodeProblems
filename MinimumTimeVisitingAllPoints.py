"""
Speed:
Space:
"""
def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        time = 0
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            
            xDiff = abs(x1 - x2)
            yDiff = abs(y1 - y2)
            
            if xDiff > yDiff:
                time += xDiff
            else:
                time += yDiff
            
        return time
            
