class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subS = ""
        ans = 0
        
        if len(s) == 1:
            return 1
        
        start = 0
        for i in range(len(s)):
            print(s[start:i+1])
            if len(set(s[start:i+1])) > len(subS):
                subS = s[start:i+1]
                ans = max(ans, len(subS))
            else:
                start += 1
        
        return ans
        