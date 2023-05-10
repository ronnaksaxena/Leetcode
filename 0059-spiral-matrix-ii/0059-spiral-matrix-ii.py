class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        output = [[0 for _ in range(n)] for _ in range(n)]
        u, d, l, r = 0, n-1, 0, n-1
        direction = 0 # 0 r, 2 d, 3 l, 4 u
        num = 1

        while num <= (n**2):
            if direction == 0:
                for i in range(l, r+1):
                    output[u][i] = num
                    num += 1
                u += 1
            elif direction == 1:
                for i in range(u, d+1):
                    output[i][r] = num
                    num += 1
                r -= 1
            elif direction == 2:
                for i in range(r, l-1, -1):
                    output[d][i] = num
                    num += 1
                d -= 1
            elif direction == 3:
                for i in range(d, u-1, -1):
                    output[i][l] = num
                    num += 1
                l += 1
            direction = (direction+1)%4
        
        return output