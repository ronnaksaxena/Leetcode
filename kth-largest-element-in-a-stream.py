import heapq
class KthLargest:
    #Time: O(NlogN)
    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        
        #O(nlogn)
        heapq.heapify(self.heap)
        
        #only need to store k largest elements in heap
        #O((n-k)(logn)) log n operation until you have k elements left
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
            
            
            
        
​
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0] #smallest elements out of the k remaining in heap
        
        
​
​
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
​
'''
[4, 5, 8, 2, 3, 5] k = 3
MAX Heap -> push the negative value to maintain max heap structure
​
​
​
'''
