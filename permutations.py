class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []
        self.helper(res,nums,nums[:],0)
        return res
    
    def helper(self,res,nums,cur: List[int],idx):
        if idx==len(nums)-1:
            res.append(cur[:])
            return
        else:
            for i in range(idx,len(nums)):
                cur[idx],cur[i] = cur[i],cur[idx]
                self.helper(res,nums,cur,idx+1)
                cur[idx],cur[i] = cur[i],cur[idx]
