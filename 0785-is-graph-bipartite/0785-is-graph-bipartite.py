class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        for node in range(len(graph)):
            # print(color)
            if node not in color:
                stack = [node]
                color[node] = 0
                while stack:
                    node = stack.pop()
                    for nei in graph[node]:
                        if nei not in color:
                            stack.append(nei)
                            color[nei] = 1 if color[node] == 0 else 0
                        elif color[nei] == color[node]:
                            # print(nei, node, color)
                            return False
        return True