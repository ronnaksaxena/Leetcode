class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = collections.defaultdict(set)
        # Create Graph O(E)
        for cityA, cityB in roads:
            graph[cityA].add(cityB)
            graph[cityB].add(cityA)
        maxRank = 0
        # Check all possible pairs O(V * V-1)
        for cityA in range(n):
            for cityB in range(cityA+1, n):
                rank = len(graph[cityA]) + len(graph[cityB])
                # If cities connected only count edge once
                if cityB in graph[cityA]:
                    rank -= 1
                maxRank = max(maxRank, rank)
        return maxRank


        