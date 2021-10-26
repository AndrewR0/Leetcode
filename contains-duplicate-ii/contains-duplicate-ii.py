import math
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        found = {}
        
        for i in range(len(nums)):
            if nums[i] in found:
                found[nums[i]].append(i)
            else:
                found[nums[i]] = [i]
        
        find = False
        for j in found.values():
            if(len(j) > 1):
                for x in range(len(j)):
                    try:
                        if(abs(j[x]-j[x+1]) <= k):
                            find = True
                            
                    except:
                        break
                if find:
                    return True
        return find