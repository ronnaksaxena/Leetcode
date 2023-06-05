class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        coordinates.sort(key = lambda x: x[0])
        # Special case horizontal line
        if coordinates[0][0] == coordinates[1][0]:
            return all(x[0] == coordinates[0][0] for x in coordinates)
        # slope = (y1-y2) / (x1-x2)
        slope = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0]-coordinates[0][0])
        
        for i in range(1, len(coordinates)-1):
            x1, y1 = coordinates[i]
            x2, y2 = coordinates[i+1]
            
            if x1 == x2 or (y2-y1)/(x2-x1) != slope:
                return False
        
        return True