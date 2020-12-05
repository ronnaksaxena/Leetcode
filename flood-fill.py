class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image:
            return image
        oldColor = image[sr][sc]
        if oldColor==newColor:
            return image
        def dfs(image,r,c):
            if r<0 or r>=len(image):
                return
            if c<0 or c>=len(image[0]):
                return
            if image[r][c]==oldColor:
                image[r][c]=newColor
                dfs(image,r+1,c)
                dfs(image,r-1,c)
                dfs(image,r,c+1)
                dfs(image,r,c-1)
        dfs(image,sr,sc)
        return image
                
            
