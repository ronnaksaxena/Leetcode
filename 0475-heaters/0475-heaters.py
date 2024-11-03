class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # Sort both houses and heaters
        houses.sort()
        heaters.sort()
        
        # To store the minimum radius
        min_radius = 0
        
        # Iterate over each house
        for house in houses:
            # Binary search to find the position of the closest heater
            pos = bisect.bisect_left(heaters, house)
            
            # Compute distances to the nearest heater (before and after)
            left_heater_distance = float('inf') if pos == 0 else house - heaters[pos - 1]
            right_heater_distance = float('inf') if pos == len(heaters) else heaters[pos] - house
            
            # Take the minimum distance of the two
            min_distance = min(left_heater_distance, right_heater_distance)
            
            # Update the radius (max of all minimum distances)
            min_radius = max(min_radius, min_distance)
        
        return min_radius
            
        