class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        '''
        equations[i] = [Ai, Bi]
        values[i] = Ai / Bi

        find Cj / Dj

        a / b = 2.0 b / c == 3.0

        a * b => a / c
        b.  c

        weights are the quotient and quotient of (startNode, endNode) is product of all weight in the path

        EDGE CASES
            - if node not present in graph: return -1
            - if divisor and dividend are eq return 1

        Clarification Qs:
            - valid values given
            - no float overflow
            - recursive stack will not exceed memory

        IDEA = DFS solution

    1. init graph and output list
        - graph[a] [(neighborB, quotient)]
        - graph[b] [(neighborA, 1/quotient)]
    2. for each query run a dfs and append quotient to output
    3. return output

    Time: O(q * (E+V))
    Space: O(E+V) for graph

        '''

        graph = collections.defaultdict(list)
        output = []

        for (a,b), q in zip(equations, values):
            graph[a].append((b, q))
            graph[b].append((a, 1/q))

        def dfs(node, target, quotientSoFar, visited):
            if node not in visited:
                if node == target:
                    return quotientSoFar
                visited.add(node)
                for nei, quot in graph[node]:
                    if nei not in visited:
                        ans = dfs(nei, target, quotientSoFar*quot, visited)
                        if ans != -1:
                            return ans
            return -1


        for start, end in queries:
            if start not in graph or end not in graph:
                output.append(-1)
            elif start == end:
                output.append(1)
            else:
                output.append(dfs(start, end, 1, set()))
        
        return output

        
        