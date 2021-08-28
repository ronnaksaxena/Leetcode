class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        DP = [ [] for _ in range(target+1)]
        
        for c in candidates:
            for i in range(1,len(DP)):
                
                if c > i: 
                    continue
                elif c == i:
                    DP[i].append([c])
                else:
                    
                    for sublist in DP[i-c]:
                        DP[i].append(sublist + [c])
                        
        return DP[-1]
                
        
