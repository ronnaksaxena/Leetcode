class TicTacToe:

    def __init__(self, n: int):
        self.p1 = {
            'col': [0 for i in range(n)],
            'row' : [0 for i in range(n)],
            'diag': 0,
            'rdiag': 0
        }
        self.p2 = {
            'col': [0 for _ in range(n)],
            'row' : [0 for _ in range(n)],
            'diag': 0,
            'rdiag': 0 # r == self.n - c
        }
        self.n = n
        '''
        x x x x
        x x x x
        x x x x
        x x x x
        
        '''
        

    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            self.p1['row'][row] += 1
            self.p1['col'][col] += 1
            if row == col:
                self.p1['diag'] += 1
            if row == self.n - col - 1:
                self.p1['rdiag'] += 1
            if self.p1['row'][row] == self.n  or self.p1['col'][col] == self.n or self.p1['diag'] == self.n or self.p1['rdiag'] == self.n:
                return 1
        else:
            self.p2['row'][row] += 1
            self.p2['col'][col] += 1
            if row == col:
                self.p2['diag'] += 1
            if row == self.n - col - 1:
                self.p2['rdiag'] += 1
            if self.p2['row'][row] == self.n  or self.p2['col'][col] == self.n or self.p2['diag'] == self.n or self.p2['rdiag'] == self.n:
                return 2
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)