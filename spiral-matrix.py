class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        spiral = []
        m = len(matrix)
        n = len(matrix[0])
        T,B,L,R = 0,m-1,0,n-1
        direc = 0
        while (T <= B and L <= R):
            if direc == 0:
                for i in range(L,R+1):
                    spiral.append(matrix[T][i])
                T += 1
            elif direc == 1:
                for i in range(T,B+1):
                    spiral.append(matrix[i][R])
                R -= 1
            elif direc == 2:
                for i in range(R, L-1, -1):
                    spiral.append(matrix[B][i])
                B -= 1
            else:
                for i in range(B, T-1, -1):
