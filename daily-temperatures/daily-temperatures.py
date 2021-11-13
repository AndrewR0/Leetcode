class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        ans = [0]*n
        
        for day in range(n): 
            while stack and temperatures[day] > temperatures[stack[-1]]:
                prev = stack.pop()
                ans[prev] = day - prev
            stack.append(day)
        return ans
        
        