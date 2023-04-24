class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = []
        for r in range(1, numRows+1):
            output.append([1 for _ in range(r)])
        
        for r in range(len(output)):
            for c in range(1, len(output[r])-1):
                output[r][c] = output[r-1][c-1] + output[r-1][c]
        
        return output
        