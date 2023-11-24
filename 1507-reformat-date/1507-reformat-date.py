class Solution:
    def reformatDate(self, date: str) -> str:
        
        day, mon, year = date.split(' ')
        day = ''.join([d for d in day if d.isnumeric()])
        # single digit
        if len(day) == 1:
            day = '0' + day
        months = {
            'Jan': '01',
            'Feb': '02',
            'Mar': '03',
            'Apr': '04',
            'May': '05',
            'Jun': '06',
            'Jul': '07',
            'Aug': '08',
            'Sep': '09',
            'Oct': '10',
            'Nov': '11',
            'Dec': '12'
            
        }
        mon = months[mon]
        return year + '-' + mon + '-' + day
        