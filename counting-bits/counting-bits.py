class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        count = 0
        
        for i in range(n+1):
            count = 0
            j = 0
            n = str(format(i,"b"))
            while j < len(n):
                if n[j] == "1":
                    count += 1
                j += 1
            ans.append(count)
            
        
        return ans