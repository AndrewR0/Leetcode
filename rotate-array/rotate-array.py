class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        n = len(nums)-1
        stack = []
        unchanged = []
        
        for i in range(n, n-k, -1):
            #print(nums[i])
            stack.append(nums[i])
        for j in range(n-k, -1, -1):
            #print(nums[j])
            unchanged.append(nums[j])
        #print(stack)
        #print(unchanged)
        
        for x in range(n+1):
            #print(x)
            #print(nums[x])
            if stack:
                nums[x] = stack.pop()
                #print(nums[x])
            elif unchanged:
                nums[x] = unchanged.pop()
                #print(nums[x])
        '''
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]
        
        
        