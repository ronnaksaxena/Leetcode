class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        # Step 1: Sort the buses and passengers
        buses.sort()
        passengers.sort()
        
        # Step 2: Assign passengers to buses
        bus_seatings = [[] for _ in range(len(buses))]
        passenger_index = 0
        m = len(passengers)
        n = len(buses)
        
        for bus_idx in range(n):
            while (passenger_index < m and 
                   passengers[passenger_index] <= buses[bus_idx] and 
                   len(bus_seatings[bus_idx]) < capacity):
                bus_seatings[bus_idx].append(passengers[passenger_index])
                passenger_index += 1
        
        # Create a set of all passenger arrival times for collision checks
        passenger_set = set(passengers)
        
        # Step 3: Determine the latest possible arrival time
        # Scenario 1: Last bus has available capacity
        if len(bus_seatings[-1]) < capacity:
            # You can arrive at the departure time of the last bus
            latest_time = buses[-1]
            # Ensure you don't arrive at the same time as any passenger
            while latest_time in passenger_set:
                latest_time -= 1
            return latest_time
        
        # Scenario 2: Last bus is full
        else:
            # The latest you can arrive is one minute before the last passenger who boarded the last bus
            last_passenger_time = bus_seatings[-1][-1]
            latest_time = last_passenger_time - 1
            # Ensure this time doesn't collide with any passenger's arrival time
            while latest_time in passenger_set:
                latest_time -= 1
            return latest_time
