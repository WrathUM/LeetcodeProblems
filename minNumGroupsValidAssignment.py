class Solution:
    def minGroupsForValidAssignment(self, balls: List[int]) -> int:
        count = Counter(balls)
        n = min(count.values())

        def canBreak(val, smallest):
            # some n times smallest and some m times (smallest+1) should be val
            # to find minimum num of boxes, maximize `m` or minimize `n`
            a = 0
            boxes = 0
            while a <= val:
                if (val-a) % (smallest+1) == 0:
                    boxes = ((val-a) // (smallest+1)) + (a // smallest)
                    break
                a += smallest
            return boxes

        while n:
            smallest = n
            boxes = 0
            for val in count.values():
                if val <= smallest+1:
                    boxes += 1
                else:
                    borken_into = canBreak(val, smallest)
                    if not borken_into:
                        break
                    boxes += borken_into
            else:
                return boxes
            n -= 1
        

