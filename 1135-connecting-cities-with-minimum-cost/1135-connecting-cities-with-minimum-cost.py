class Solution(object):
    def minimumCost(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        parent = [i for i in range (n+1)]
        rank = [0] *(n+1)
        
        def find(n1):
            p1 = parent[n1]
            while p1 != parent[p1]:
                parent[p1] = parent[parent[p1]]
                p1 = parent[p1]
            return p1
        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            if p1 == p2 :
                return False
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True
        connections = sorted(connections,key= lambda x:x[2])
        output = 0
        no_of_disconnected_graphs = n
        for edge in connections:
            if union(edge[0],edge[1]) == True:
                output += edge[2]
                no_of_disconnected_graphs -= 1
                if no_of_disconnected_graphs == 1:
                    return output
        return -1
     