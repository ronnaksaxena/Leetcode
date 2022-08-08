class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        graph = collections.defaultdict(list)
        in_degree = collections.defaultdict(int)
        
        for r,ing in zip(recipes,ingredients):
            
            # Find in degree and nodes ingredients point to
            for i in ing:
                # ing -> recipes
                graph[i].append(r)
                # How many nodes point to r
                in_degree[r] += 1
        
        #populate queue with supplies since we know their in_degree is 0
        queue = supplies[::]
        res = []
        while queue:
            
            cur = queue.pop(0)
            # found a recipe
            if cur in recipes:
                res.append(cur)
                
            for neighbor in graph[cur]:
                in_degree[neighbor] -= 1
                # Can remove node from graph
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return res
                    
                    
                    
                    
                    
        
