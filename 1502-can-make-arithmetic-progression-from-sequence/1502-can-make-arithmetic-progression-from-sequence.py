class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        return all(arr[1]-arr[0] == arr[i+1]-arr[i] if i != len(arr)-1 else True for i,_ in enumerate(arr))
        