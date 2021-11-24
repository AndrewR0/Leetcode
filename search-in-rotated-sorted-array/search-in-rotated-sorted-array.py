class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if(len(nums) == 1 and nums[0] == target):
            return 0
        if(len(nums) == 1 and nums[0] != target):
            return -1
        
        lower = 0
        upper = len(nums)-1
        
        while upper >= lower:
            mid = (lower + upper)//2
            
            #print(mid)
            if(nums[mid] == target):
                return mid
            
            if nums[mid] >= nums[lower]:
                if nums[lower] <= target <= nums[mid]:
                    upper = mid - 1
                else:
                    lower = mid + 1
            else:
                if nums[mid] <= target <= nums[upper]:
                    lower = mid + 1
                else:
                    upper = mid - 1
        return -1
        '''
        elif(nums[mid] >= nums[lower] and nums[lower] > target):
            print("1")
            lower = mid + 1
        elif(nums[mid] >= nums[lower] and nums[lower] < target < nums[mid]):
            print("2")
            upper = mid - 1
        elif(nums[mid] <= nums[lower] and nums[mid] > target):
            print("3")
            #lower = mid + 1
            upper = mid - 1
        elif(nums[mid] <= nums[lower] and nums[mid] < target):
            print("4")
            #upper = mid - 1
            lower = mid + 1
        elif(nums[lower] == target):
            print("5")
            return lower
        elif(lower == upper and nums[lower] != target):
            print("6")
            return -1
        else:
            lower = mid + 1
        '''