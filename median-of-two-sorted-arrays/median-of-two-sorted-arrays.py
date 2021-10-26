import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums3 = nums1 + nums2
        nums3.sort()
        print(nums3)
        middle = 0
        if(len(nums3) % 2 == 0):
            middle = (nums3[int(len(nums3)/2)] + nums3[int(len(nums3)/2) - 1])/2
            print("if",middle)
        else:
            middle = nums3[math.floor(len(nums3)/2)]
            print("else",middle)
        
        return middle
        #Original code ^^^
        
        #return median(sorted(nums1+nums2))