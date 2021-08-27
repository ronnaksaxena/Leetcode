class Solution:
    def validIPAddress(self, IP: str) -> str:
        if self.isIPv4(IP):
            return 'IPv4'
        elif self.isIPv6(IP):
            return 'IPv6'
        else:
            return 'Neither'
        
        
    def isIPv4(self, IP):
        blocks = IP.split('.')
        
        if len(blocks) != 4:
            return False
        
        for s in blocks:
            print(s)
            if len(s) < 1 or len(s) > 4:
                return False
            
            if s[0] == '0' and len(s) > 1:
                return False
            
            for c in s:
                if not c.isnumeric():
                    return False
                
            if not 0 <= int(s) <= 255:
                return False
            
        return True
    
    def isIPv6(self,IP):
        blocks = IP.split(':')
        valids = {'a','b','c','d','e','f'}
        
        if len(blocks) != 8:
            return False
        
        for s in blocks:
            
            if len(s) < 1 or len(s) > 4:
                return False
            for c in s:
                if not c.isnumeric() and not c.lower() in valids:
                    return False
                
        return True
            
            
            
