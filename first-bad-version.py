# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):
​
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        l , r = 1, n
        
        while l < r:
            mid = l + (r-l)//2
            isBad = isBadVersion(mid)
            
            if isBad and (mid==1 or not isBadVersion(mid-1)):
                return mid
            
            elif isBad:
                r = mid-1
            
            else:
                l = mid + 1
                
        return l
            
            
            
            
            
