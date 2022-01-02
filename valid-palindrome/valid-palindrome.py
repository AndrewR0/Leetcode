class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        check = [i.lower() for i in s if i.isalnum()]
        #print(check)
        
        return check == check[::-1]