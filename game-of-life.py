        
        #first pass
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 1:
                    for di,dj in neighbors:
                        newR,newC = i+di,j+dj
                        if 0 <= newR < m and 0 <= newC < n:
                            if board[newR][newC] > 0: board[i][j] += 1
                    
                else: #is 0
                    for di,dj in neighbors:
                        newR,newC = i+di,j+dj
                        if 0 <= newR < m and 0 <= newC < n:
                            if board[newR][newC] > 0: board[i][j] -= 1
​
        
        #seconds pass
        for i in range(m):
            for j in range(n):
                if board[i][j] in {-3,3,4}:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
                    
                    
        return
                    
