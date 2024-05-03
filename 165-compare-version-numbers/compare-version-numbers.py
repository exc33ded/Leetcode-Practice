class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        verLst1 = list(int(v) for v in version1.split("."))
        verLst2 = list(int(v) for v in version2.split("."))

        for i in range(max(len(verLst1), len(verLst2))):
            if i < len(verLst1):
                v1 = verLst1[i]
            else:
                v1 = 0
            
            if i < len(verLst2):
                v2 = verLst2[i]
            else:
                v2 = 0
            
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
    
        return 0