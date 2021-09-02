class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        output = ''
        
        for s in strs:
            output += str(len(s)) + '#' + s
        return output
​
    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        output = []
        i = 0
        while i < len(s):
            j  = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            output.append(s[j+1:j+1+length])
            i = j + 1 + length
            
        return output
​
​
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
