class Robot():
    def __init__(self, position, health, direction, io):
        self.position = position
        self.health = health
        self.direction = direction
        self.inputOrder = io
        
    def isDead(self):
        if self.health == 0:
            return True
        return False
    

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = []
        direct = list(directions)
        
        for i, (p,h,d) in enumerate(zip(positions, healths, direct)):
            robots.append(Robot(p,h,d,i))
        
        robots.sort(key = lambda x: x.position)
        
        stack = []
        
        for r in robots:
            if r.direction == "R":
                stack.append(r)
            elif stack and stack[-1].direction == 'R':
                # compute winner
                while not r.isDead():
                    if not stack or stack[-1].direction == 'L':
                        stack.append(r)
                        break
                    
                    if r.health > stack[-1].health:
                        # print("Hello")
                        stack.pop()
                        r.health -= 1
                    elif r.health < stack[-1].health:
                        stack[-1].health -= 1
                        r.health = 0
                    else:
                        r.health = 0
                        stack[-1].health = 0
                        stack.pop()
            else:
                stack.append(r)
            
        print(stack)
        stack.sort(key = lambda x: x.inputOrder)
        res = []
        for r in stack:
            res.append(r.health)
        return res
