class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = str(x)[::-1]
        try:
            if int(rev) == x:
                return True
        except:
            return False
        return False
        #return str(x) == str(x)[::-1]
        