class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        totDist, d = 0, float('-inf')
        for nut in nuts:
            totDist += self.dist(nut, tree)*2
            d = max(d, self.dist(nut,tree)-self.dist(nut,squirrel))
        return totDist-d
    
    def dist(self, a, b):
        return abs(a[0]-b[0])+abs(a[1]-b[1])
