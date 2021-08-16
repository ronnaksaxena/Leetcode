class Solution:
    def nextClosestTime(self, time: str) -> str:
        minutes = (int(time[:2]) * 60) + (int(time[3:]))
        digits = {d for d in time if d.isnumeric()}
        
        while True:
​
            minutes = (minutes+1) % (24*60)
​
            minuteArr = [(minutes//60)//10, (minutes//60)%10, (minutes%60)//10, (minutes%60)%10]
​
            isValid = True
            for d in minuteArr:
                if str(d) not in digits:
                    isValid = False
​
            if isValid:
                return str(minuteArr[0]) + str(minuteArr[1]) + ':' + str(minuteArr[2]) + str(minuteArr[3])
         
​
