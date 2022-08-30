class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magDict = {}
        for i in magazine:
            if i in magDict:
                magDict[i] += 1
            else:
                magDict[i] = 1
        
        ranDict = {}
        for j in ransomNote:
            if j in ranDict:
                ranDict[j] += 1
            else:
                ranDict[j] = 1
        
        keyList = list(ranDict.keys())
        
        k = 0
        while k != len(keyList):
            if keyList[k] not in magDict or ranDict[keyList[k]] > magDict[keyList[k]]:
                return False
            k += 1
        return True
        
            