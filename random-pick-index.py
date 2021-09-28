class Solution:
    '''
    i n
    1   i     i+1    n-1
    i   i+1   i+2     n
    
    '''
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
​
    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        res = None
        count = 0
        for i, n in enumerate(self.nums):
            if n == target:
                num = random.randint(0, count)
                if num == 0:
                    res = i
                count += 1
        return res
​
    
        
​
​
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
