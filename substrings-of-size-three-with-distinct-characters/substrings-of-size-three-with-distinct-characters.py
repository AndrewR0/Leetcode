class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        #dic = {}
        subS = ""
        ans = 0
        
        if len(s) < 3:
            return 0

        for i in range(3):
            subS += s[i]
        
        if len(set(subS)) == len(subS):
            ans += 1
        for j in range(len(s)-3):
            
            subS = s[j+1] + s[j+2] + s[j+3]
            
            if len(set(subS)) == len(subS):
                ans += 1
            
        return ans