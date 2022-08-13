class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        # If odd no possible split
        if finalSum%2:
            return []
        ans = []
        i = 2
        curSum = 0
        # Add smallest possible even nums first
        # Stop  before an extra additon would overflow finalSum
        while curSum+i <= finalSum:
            ans.append(i)
            curSum += i
            i += 2
        # Increment last int by remaining difference
        ans[-1] += (finalSum - curSum)
        return ans
    
    # Time: O(n) to loop through half of digits in finalSum in worst case
    # Space: O(n): to store all digits
        
