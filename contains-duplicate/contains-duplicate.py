class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''found = {}
        
        for i in nums:
            if i in found:
                return True
            else:
                found[i] = 1
        return False
        '''
        return len(set(nums)) != len(nums)