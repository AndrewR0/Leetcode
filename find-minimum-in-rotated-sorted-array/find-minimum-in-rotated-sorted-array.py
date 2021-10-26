import math
class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if(len(nums) == 1):
            return nums[0]
        
        if(nums[0] < nums[len(nums)-1]):
            return nums[0]
        
        lower = 0
        upper = len(nums)-1
        
        while True:
            mid = (lower+upper)//2
            
            
            if(nums[mid] > nums[mid+1]):
                return nums[mid+1]
            if(nums[mid] < nums[mid-1]):
                    return nums[mid]
            if(nums[mid] > nums[0]):
                lower = mid + 1
            else:     
                upper = mid - 1
            