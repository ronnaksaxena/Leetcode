class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emToName = {}
        graph = collections.defaultdict(set)

        # Build the graph by connecting all emails in the same account
        for a in accounts:
            name = a[0]
            first_email = a[1]
            for em in a[1:]:
                graph[first_email].add(em)
                graph[em].add(first_email)
                emToName[em] = name

        visited = set()
        output = []
        for node in graph:
            if node in visited:
                continue

            # Use DFS to traverse all connected emails and merge them
            sameAccounts = []
            stack = [node]
            while stack:
                cur = stack.pop()
                if cur in visited:
                    continue
                sameAccounts.append(cur)
                visited.add(cur)
                for nei in graph[cur]:
                    if nei not in visited:
                        stack.append(nei)

            output.append([emToName[node]] + sorted(sameAccounts))

        return output
