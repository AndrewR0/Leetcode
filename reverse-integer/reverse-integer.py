import math
class Solution:
    def reverse(self, x: int) -> int:
        strInt = str(x)
        rev = strInt[::-1]
        #return rev[-1]
        if rev[-1] == "-":
            rev = rev[:len(rev)-1]
            rev = "-" + rev
        if int(rev) > math.pow(2,31)-1 or int(rev) < math.pow(-2, 31):
            return 0
        return int(rev)