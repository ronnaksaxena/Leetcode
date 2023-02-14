class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        # Store the number of cities (including the capital city)
        n = len(roads) + 1
        
        # Create an adjacency list to store the roads between cities
        adj = [[] for _ in range(n)]
        
        # Store the degree (number of roads) for each city
        degree = [0] * n

        # Loop through all the roads
        for road in roads:
            # Add the roads to the adjacency list
            adj[road[0]].append(road[1])
            adj[road[1]].append(road[0])
            
            # Increase the degree of both cities connected by the road
            degree[road[0]] += 1
            degree[road[1]] += 1

        # Create a queue for BFS
        q = deque()
        
        # Add all cities with degree 1 (i.e., only one road) to the queue
        for i in range(1, n):
            if degree[i] == 1:
                q.append(i)

        # Store the number of representatives for each city
        representatives = [1] * n
        # Initialize the fuel cost to 0
        fuel = 0
        # Start BFS
        while q:
            # Get the next node from the queue
            node = q.popleft()
            # Calculate the fuel cost for visiting this city
            # Divide by seats because it takes 1 liter to fuel everyone in car
            fuel += math.ceil(representatives[node] / seats)
            
            # Loop through all neighbors of the current node
            for neighbor in adj[node]:
                # Decrease the degree of the neighbor
                degree[neighbor] -= 1
                
                # Add the representatives of the current node to the neighbor
                representatives[neighbor] += representatives[node]
                
                # If the neighbor now has degree 1, add it to the queue for BFS
                if degree[neighbor] == 1 and neighbor != 0:
                    q.append(neighbor)

        # Return the total fuel cost
        return fuel