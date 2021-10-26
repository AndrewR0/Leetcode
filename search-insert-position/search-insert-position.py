class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        first = 0
        last = len(nums) - 1
        
        while first <= last:
            mid = int((first + last)/2)
            
            if nums[mid] == target:
                return mid
            
            elif first == len(nums)-1:
                if nums[mid] > target:
                    return mid
                return len(nums)
                
            
            elif last == 0:
                if nums[mid] > target:
                    return mid
                else:
                    return mid+1
            
            else:
                if nums[mid] > target:
                    if mid == 0:
                        return mid
                    elif nums[mid-1] < target:
                        return mid
                    last = mid-1
                elif nums[mid] < target:
                    if nums[mid+1] > target:
                        return mid+1
                    first = mid+1
            
            


        
            