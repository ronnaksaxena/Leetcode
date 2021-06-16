class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        adjList = collections.defaultdict(list)
        
        for pre, post in tickets:
            adjList[pre].append(post)
            
        for l in adjList.keys():
            adjList[l].sort()
        
        order = collections.deque()
        
        def helper(node):
            while adjList[node]:
                helper(adjList[node].pop(0))
            order.appendleft(node)
            
        helper('JFK')
        return order
        
