class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        '''
        supplies : "yeast" "flour" "meat"
                     \.     /        /
                        bread       /
                          \        /
                              sandwich
        recipies : bread, sandwich

Time: O(E+V) or O(repicies + ingredients)
Space: O(V)
        '''
        inDegree = collections.defaultdict(int)
        graph = collections.defaultdict(list)

        for rec, ing in zip(recipes, ingredients):
            for i in ing:
                graph[i].append(rec)
                inDegree[rec] += 1
        q = collections.deque()
        for s in supplies:
            q.append(s)
        output = []
        while q:
            node = q.popleft()
            if node in recipes:
                output.append(node)
            for nei in graph[node]:
                inDegree[nei] -= 1
                if inDegree[nei] == 0:
                    q.append(nei)

        return output




