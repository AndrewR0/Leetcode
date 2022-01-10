class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        curDir = 0 #0:N, 1:E, 2:S, 3:W
        
        for i in instructions:
            if i == "G":
                if curDir == 0:
                    y += 1
                if curDir == 1:
                    x += 1
                if curDir == 2:
                    y -= 1
                if curDir == 3:
                    x -= 1        
            if i == "L":
                if curDir - 1 < 0:
                    curDir = 3
                else:
                    curDir -= 1
            if i == "R":
                if curDir + 1 > 3:
                    curDir = 0
                else:
                    curDir += 1
        return curDir != 0 or (x,y) == (0,0)