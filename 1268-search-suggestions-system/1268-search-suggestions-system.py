class Node:
    def __init__(self, endOfWord=False):
        self.endOfWord = endOfWord
        self.children = {}

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Insert word into trie
        def insertIntoTrie(root, word):
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = Node()
                cur = cur.children[c]
            cur.endOfWord = True

        # Find up to 3 suggested products based on prefix
        def findSuggestedProducts(node, pre):
            results = []

            # Helper function for DFS to collect up to 3 words
            def dfs(node, wordSoFar):
                nonlocal results
                if node.endOfWord:
                    results.append(''.join(wordSoFar))
                    if len(results) == 3:
                        return

                # Continue DFS with lexicographically smaller children
                for nextChar in sorted(node.children.keys()):
                    dfs(node.children[nextChar], wordSoFar + [nextChar])
                    if len(results) == 3:
                        return

            cur = node
            for c in pre:
                if c in cur.children:
                    cur = cur.children[c]
                else:
                    return []  # No matching prefix, return empty list
            dfs(cur, [c for c in pre])  # Start DFS from current node
            return results

        # Build the trie
        root = Node()
        for p in products:
            insertIntoTrie(root, p)

        # Collect suggested products for each prefix of searchWord
        output = []
        for i in range(1, len(searchWord) + 1):
            output.append(findSuggestedProducts(root, searchWord[:i]))
        
        return output
