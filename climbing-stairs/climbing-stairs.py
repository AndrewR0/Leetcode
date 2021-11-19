class Solution:
    
    def climbStairs(self, n: int, nums={}) -> int:     
        
        if n in nums:
            return nums[n]
        if n == 0:
            return 1
        if n < 0:
            return 0
        nums[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return nums[n]
        