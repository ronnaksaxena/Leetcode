class Solution:
    def alienOrder(self, words: List[str]) -> str:

        '''
        w - > e
        t -> f

        1. iterate thorugh words and construct graph
            - aab, aa
        2. find top ordering of letter
        3. check we were able to traverse every letter

        Time: O(E+V) or O(number of words - 1 + letters in words)
        Space: O(V) or O(letters)
        '''

        graph = collections.defaultdict(set)
        inDegree = collections.defaultdict(int)
        for word in words:
            for c in word:
                if c not in graph:
                    graph[c] = set()
                if c not in inDegree:
                    inDegree[c] = 0
        # Looking for relationship of letters form words
        for first, second in zip(words, words[1:]):
            # Handle edge case ex. aab, aa
            foundEdge = False
            for f, s in zip(first, second):
                if f != s:
                    foundEdge = True
                    # Only want to add letter relationship once
                    if s not in graph[f]:
                        graph[f].add(s)
                        inDegree[s] += 1
                    break
            if not foundEdge and len(second) < len(first):
                # No ordering exists
                return ''
        order = []
        q = collections.deque()
        for c in inDegree:
            if inDegree[c] == 0:
                q.append(c)
        while q:
            letter = q.popleft()
            order.append(letter)
            for nextLetter in graph[letter]:
                inDegree[nextLetter] -= 1
                if inDegree[nextLetter] == 0:
                    q.append(nextLetter)
        # If you could traverse all letters, ordering exists
        return ''.join(order) if len(order) == len(graph.keys()) else ''

        



