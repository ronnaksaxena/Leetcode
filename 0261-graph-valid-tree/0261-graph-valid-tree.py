class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        input: n:int, edges: List of List int
        output: bool

        -len(edges) == n
        -n can be 0
        -node cannot point to itself

        parent -> child relationshp which means NO CYCLES

        Algo: Traverse graph and any neighbors (EXCLUDING PARENT) have been visited there is a cycle

                4
             /    \. \
             1.   2.   3
             /
             0

        helper fn isParent(child, parent):
            return child in edges[parent]

        if any neighbors have been visted and are not parent of node return False

        PSUEDOCODE

        stack = [0]
        visited = set{0}

        while stack:
            cur = stack.pop()
            visited.add(cur)
            for neighbor in edges[cur]:
                if neighbor in visited and not isParent(cur, neighbor):
                    return False
                stack.append(neighbor)


        return len(visited) == n
        '''
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node, parent, visited):
            if node in visited:
                return False
            visited.add(node)
            for nei in graph[node]:
                if nei != parent:
                    if not dfs(nei, node, visited):
                        return False
            return True
        visited = set()
        return dfs(0, -1, visited) and len(visited) == n

        