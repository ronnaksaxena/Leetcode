class DetectSquares:
​
    def __init__(self):
        # (X, Y) : frequency
        self.points = collections.defaultdict(int)
        
​
    def add(self, point: List[int]) -> None:
        self.points[(point[0], point[1])] += 1
        
​
    def count(self, point: List[int]) -> int:
        count = 0
        pX, pY = point[0], point[1]
        for x,y in self.points.keys():
            # Found point on same y axis
            if y == pY and x != pX:
                # Find length of edges
                dist = abs(pX-x)
                # Check if square can be formed using line as bottom edge
                if (min(pX,x), y+dist) in self.points and (max(pX,x), y + dist) in self.points:
                    squares = (self.points[(min(pX,x), y+dist)]) * (self.points[(max(pX,x), y + dist)]) * (self.points[x,y])
                    count += squares
                # Check if square can be formed using line as a top edge
                if (min(pX, x), y-dist) in self.points and (max(pX, x), y-dist) in self.points:
                    squares = (self.points[(min(pX, x), y-dist)]) * (self.points[(max(pX, x), y-dist)]) * (self.points[x,y])
                    count += squares
        return count
                
        
​
​
# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
​
'''
map = {(pX, pY), freq)}
