class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        low = 0
        high = len(nums)-1
        
        for i in range(len(nums)):
            mid = (low+high)//2
            
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                low = mid+1
            else:
                high = mid-1
        return -1