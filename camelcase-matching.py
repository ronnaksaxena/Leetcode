import re
​
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        
        output = []
        
        find = re.compile(r'^[a-z]*'+'[a-z]*'.join(list(pattern))+'[a-z]*$')
        for w in queries:
            match = re.search(find,w)
            if match:
                output.append(True)
            else:
                output.append(False)
        
        return output
        
