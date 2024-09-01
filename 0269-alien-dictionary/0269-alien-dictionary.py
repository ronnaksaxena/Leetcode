class Solution:
    def alienOrder(self, words: List[str]) -> str:
        in_degree = {}
        graph = {}

        for w in words:
            for c in w:
                in_degree[c] = 0
                graph[c] = []

        numLetters = len(in_degree)
        
        for first, second in zip(words, words[1:]):
            # Find first letter that differs
            difLetter = None
            for a, b in zip(first, second):
                if a != b:
                    difLetter = a
                    in_degree[b] += 1
                    graph[a].append(b)
                    break
            if len(second) < len(first) and not difLetter:
                # No order possible
                return ''
        
        q = collections.deque()
        for letter, deg in in_degree.items():
            if not deg:
                q.append(letter)
        
        order = []
        while q:
            cur = q.popleft()
            order.append(cur)

            for nextLetter in graph[cur]:
                in_degree[nextLetter] -= 1
                if not in_degree[nextLetter]:
                    q.append(nextLetter)
        
        return ''.join(order) if len(order) == numLetters else ''

        