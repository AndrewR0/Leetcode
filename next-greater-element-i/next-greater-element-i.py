class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        
        for i in nums1:
            for j in nums2[nums2.index(i):]:
                if j > i:
                    ans.append(j)
                    break
                elif (nums2.index(j)+1) == len(nums2):
                    ans.append(-1)
        return ans
                    