class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        found = {}
        
        for i in nums:
            if i in found:
                #found[i] += 1
                return True
            else:
                found[i] = 1
        return False