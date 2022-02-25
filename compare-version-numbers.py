class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        v1 = version1.split(".")
        v2 = version2.split(".")
        n1 = len(v1)
        n2 = len(v2)
        for i in range(min(n1,n2)):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1       
        if n1 > n2:
            compare1 = '.'.join([str(int(x)) for x in v1[n2:]])
            compare2 = '.'.join(['0' for _ in range(n1-n2)])
        elif n2 > n1:
            compare2 = '.'.join([str(int(x)) for x in v2[n1:]])
            compare1 = '.'.join(['0' for _ in range(n2-n1)])
        else:
            return 0
        if compare1 > compare2:
