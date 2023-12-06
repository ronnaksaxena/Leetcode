class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        '''
        adj List of node: {neighbors}
        
        loop through all pairs
        0: {1, 3}
        1: {0, 2, 3}
        
        maxRank is length of superset
        if cityA and cityB in superset - 1
        
        '''
        
        graph = collections.defaultdict(set)
        for a, b in roads:
            graph[a].add(b)
            graph[b].add(a)
        
        maxRank = 0
        for i in range(n):
            for j in range(i+1, n):
                rank = len(graph[i]) + len(graph[j])
                if i in graph[j] and j in graph[i]:
                    rank -= 1
                maxRank = max(rank, maxRank)
        return maxRank
                    