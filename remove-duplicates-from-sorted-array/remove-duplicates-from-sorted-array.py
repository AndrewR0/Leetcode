class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        check = {}
        
        i = 0
        while i != len(nums):
            if(nums[i] in check):
                #print("if",i)
                nums.remove(nums[i])
            else:
                #print("else",i)
                check[nums[i]] = 1
                i += 1
                
        return len(nums)