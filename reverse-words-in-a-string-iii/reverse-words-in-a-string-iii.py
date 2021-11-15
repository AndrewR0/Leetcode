class Solution:
    def reverseWords(self, s: str) -> str:
        newS = s.split(' ')
        
        for i in range(len(newS)):
            newS[i] = newS[i][::-1]
        return ' '.join(newS)