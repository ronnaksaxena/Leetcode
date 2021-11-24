class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        
        # Preprocess the height of the warehouse rooms to get usable heights
        for i in range(1, len(warehouse)):
            warehouse[i] = min(warehouse[i - 1], warehouse[i])
​
        # Iterate through boxes from the smallest to the largest
        boxes.sort()
​
        count = 0
​
        for room in reversed(warehouse):
            # Count the boxes that can fit in the current warehouse room
            if count < len(boxes) and boxes[count] <= room:
                count += 1
​
        return count
                        
                
                        
