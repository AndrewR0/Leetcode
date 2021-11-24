class Solution:
    def maxArea(self, height: List[int]) -> int:
        curMax = 0
        left = 0
        right = len(height)-1
        
        while left <= right:
            
            l = right - left
            h = min(height[left], height[right])
            
            curMax = max(curMax, l*h)
            
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return curMax
        