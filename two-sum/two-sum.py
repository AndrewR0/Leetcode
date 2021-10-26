class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ls = {}
        out = []
        
        for i in range(len(nums)):
            print(target-nums[i])
            if((target - nums[i]) in ls):
                out.append(ls[target-nums[i]])
                ls[nums[i]] = i
                out.append(ls[nums[i]])
                #out.sort()
                break
            else:
                ls[nums[i]] = i
        #print(ls)
        return out