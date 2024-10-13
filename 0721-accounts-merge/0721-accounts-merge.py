class UnionFind:
    def __init__(self, n, names):
        self.par = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
        self.names = {i: name for i, name in enumerate(names)}
    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    def union(self, x, y):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False  # No union needed, they are already in the same component
        # Union by rank
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p2] = p1
            self.rank[p1] += 1 # Only have to change rank if a tie
        return True  # Return True only if a union occurred (i.e., two different components merged)
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        '''
        input: List[List[str]]
        ouptut: List[List[str]] -> [["name", account1, account2...]]
        - each list element is valid
            - each name has at least 1 account
        - a@gmail.com != A@gmail.com
        - alphanumeric chars in account name

        EDGE CASES:
        - 2 separate accounts with duplicate names: [[name: accounts with first name], [name: accoutn with second]]
        - If lenght of input is <= 1 return input


        accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John",      "johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]

        ["johnsmith@mail.com"] <-> "john_newyork@mail.com"]
        ^                       ^
        |                       |
        v                       v
            "johnnybravo@mail.com"


        "mary@mail.com"
        }

        Approach union find
        parents are indices
        nested loop through all accounts and union
        '''
        graph = collections.defaultdict(list)

        for a in accounts:
            
            for i in range(1, len(a)):
                for j in range(i+1, len(a)):
                    graph[a[i]].append(a[j])
                    graph[a[j]].append(a[i])

        
        visited = set()
        output = []

        for a in accounts:
            if a[1] in visited:
                continue
            
            name = a[0]
            q = collections.deque([a[1]])
            visited.add(a[1])
            newGroup = []

            while q:
                newAccount = q.popleft()
                newGroup.append(newAccount)
                for nei in graph[newAccount]:
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
            output.append([name] + sorted(newGroup))

        return output


        