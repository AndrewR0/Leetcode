class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        left = 0
        right = len(nums)-1
        
        while True:
            mid = (left + right)//2
            print(mid)
            
            if mid == len(nums)-1 or (nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]):
                return nums[mid]
            
            elif nums[mid] == nums[mid-1] and nums[mid] != nums[mid+1]:
                if mid % 2 == 0:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if mid % 2 != 0:
                    right = mid - 1
                else:
                    left = mid + 1
            