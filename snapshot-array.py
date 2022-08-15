class SnapshotArray:
​
    def __init__(self, length: int):
        self.SA = { i : {0 : 0} for i in range(length)} # {i : {snapID : arrVal}}
        self.snapID = 0
        
​
    def set(self, index: int, val: int) -> None:
        self.SA[index][self.snapID] = val
​
    def snap(self) -> int:
        self.snapID += 1
        return self.snapID - 1 # since just incremented
        
​
    def get(self, index: int, snap_id: int) -> int:
        while snap_id > 0 and snap_id not in self.SA[index]:
            snap_id -= 1
        return self.SA[index][snap_id]
​
        
'''
{i : {snapID : arrVal}} => gets updated in set
snapID = 0
snap will update snapID and return snapID -1
​
get: decriment snap_id arg until found valid snap_id for that index in our SA
'''
​
​
