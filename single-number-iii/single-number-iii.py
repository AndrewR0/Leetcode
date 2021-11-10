class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        numDict = {}
        ans = []
        
        for i in nums:
            if i in numDict:
                numDict[i] += 1
            else:
                numDict[i] = 1
        for j in numDict.keys():
            if numDict[j] == 1:
                ans.append(j)
        return ans
        