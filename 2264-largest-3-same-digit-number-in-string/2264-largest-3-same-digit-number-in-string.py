class Solution:
    def largestGoodInteger(self, num: str) -> str:
        idx = 1
        count = 1
        largest = -inf
        while idx < len(num):
            if num[idx] == num[idx-1]:
                count +=1
                if count == 3 and int(num[idx]) > largest:
                    largest = int(num[idx])
            else:
                count = 1
                    
            idx += 1
            
        return str(largest) * 3 if largest != -inf else ''