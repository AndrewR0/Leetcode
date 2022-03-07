class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        
        i = 0
        check = 0
        for j in range(len(t)):
            if t[j] == s[i]:
                check += 1
                i += 1
            if check == len(s):
                return True
        
        return False
            