        
        def goBack():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        
        
         
        
        def backtrack(r,c,d):
            robot.clean()
            
            for i in range(4):
                
                newD = (d + i)%4
                
                newR = r + direc[newD][0]
                newC = c + direc[newD][1]
                
                if (newR,newC) not in visited and robot.move():
                    visited.add((newR,newC))
                    backtrack(newR,newC,newD)
                    goBack()
                    
                robot.turnRight()
                
        direc = [(-1,0),(0,1),(1,0),(0,-1)]
        visited = set()        
        visited.add((0,0))
        backtrack(0,0,0)
                
                
            
            
