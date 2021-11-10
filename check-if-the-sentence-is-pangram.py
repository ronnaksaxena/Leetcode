class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphas = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
        
        for c in sentence:
            if c in alphas:
                alphas.remove(c)
                
        return not alphas
        
