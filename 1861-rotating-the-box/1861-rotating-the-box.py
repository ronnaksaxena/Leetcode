class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        boxRows, boxCols = len(box), len(box[0])
        rotated = [['.' for _ in range(boxRows)] for _ in range(boxCols)]
        # Check stones in that row
        for bR in range(boxRows):
            stones = 0
            # Loop until you find wall or reach end
            for bC in range(boxCols):
                if box[bR][bC] == '#':
                    stones += 1
                elif box[bR][bC] == '*':
                    rotated[bC][bR] = '*'
                    rotatedR, rotatedC = bC-1, bR
                    while stones > 0:
                        rotated[rotatedR][rotatedC] = '#'
                        stones -= 1
                        rotatedR -= 1
                        
            # Check if any stones left
            rotatedR, rotatedC = len(rotated)-1, bR
            # print(stones, rotated)
            while stones > 0:
                # print(rotatedR, rotatedC)
                rotated[rotatedR][rotatedC] = '#'
                stones -= 1
                rotatedR -= 1
        
        return [list(reversed(row)) for row in rotated]
                        
            
            
        