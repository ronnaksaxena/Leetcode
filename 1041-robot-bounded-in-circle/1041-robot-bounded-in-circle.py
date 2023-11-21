class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        direc = 0 # 0 is n, 1 is r, 2 is s, 3 is l. => %4
        # Simulate
        for _ in range(4):
            for i in instructions:
                if i == 'G':
                    if direc == 0:
                        y += 1
                    elif direc == 1:
                        x += 1
                    elif direc == 2:
                        y -= 1
                    else:
                        x -= 1
                elif i == 'L':
                    direc = (direc-1)%4
                else:
                    # R
                    direc = (direc+1)%4
        # Not a limit cycle
        return x == 0 and y == 0 and direc == 0
'''
Time: O(n)
Space: O(1)
'''
        