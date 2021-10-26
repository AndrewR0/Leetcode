# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1:
            return n
        
        first = 1
        last = n

        
        while first <= last:
            mid = int((first + last)/2)
            
            if isBadVersion(mid) == True and isBadVersion(mid-1) == False:
                return mid
            
            if isBadVersion(mid):
                last = mid-1
            else:
                first = mid+1
        