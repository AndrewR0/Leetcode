class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = {}
        #ans = []
        
        for count,val in enumerate(numbers):
            if target-val in nums:
                return [nums[target-val]+1, count+1]
            nums[val] = count
            