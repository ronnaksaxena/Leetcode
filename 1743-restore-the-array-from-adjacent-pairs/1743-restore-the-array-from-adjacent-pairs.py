
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        neighbors = collections.defaultdict(list)
        for u, v in adjacentPairs:
            neighbors[u].append(v)
            neighbors[v].append(u)
        # First node should only have 1 neighbor
        firstNode = None
        for val, nei in neighbors.items():
            if len(nei) == 1:
                firstNode = val
                break
        # Do a DFS on firstNode
        nums = []
        visited = set()
        stack = [firstNode]
        while stack:
            cur = stack.pop()
            if cur not in visited:
                nums.append(cur)
                visited.add(cur)
                for n in neighbors[cur]:
                    if n not in visited:
                        stack.append(n)
        return nums
            
            