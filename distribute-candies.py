class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candySet = set(candyType)
        numOfCandy = len(candyType)//2
        return len(candySet) if len(candySet)<numOfCandy else numOfCandy
