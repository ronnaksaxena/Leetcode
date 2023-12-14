class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, d = 0, 0, 0
        # d 0 is up, 1 is right, 2 is down, 3 is left
        for _ in range(4):
            for m in instructions:
                if m == 'G':
                    if d == 0:
                        # up
                        y += 1
                    elif d == 1:
                        # right
                        x += 1
                    elif d == 2:
                        # down
                        y -= 1
                    else:
                        # left
                        x -= 1
                elif m == 'L':
                    # turn left
                    d = d-1 if d > 0 else 3
                else:
                    # turn right
                    d = d + 1 if d < 3 else 0
        return x == 0 and y == 0
        