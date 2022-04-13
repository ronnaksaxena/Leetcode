                for j in range(l,r+1):
                    matrix[u][j] = cur
                    cur += 1
                u += 1
                    
            elif dir == 1:
                for i in range(u,d+1):
                    matrix[i][r] = cur
                    cur += 1
                r -= 1
            elif dir == 2:
                for j in range(r,l-1, -1):
                    matrix[d][j] = cur
                    cur += 1
                d -= 1
            else:
                for i in range(d,u-1, -1):
                    matrix[i][l] = cur
                    cur += 1
                l += 1
            dir = (dir+1)%4
            
        return matrix
                    
                    
                    
                    
                    
                
                
                
                
                
                
                
                
