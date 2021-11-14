class Solution:
    def isHappy(self, n: int) -> bool:
        
        temp = 0
        created = {}
        
        #if n < 9 and n != 1:
        #    return False
        
        while True:
            for i in str(n):
                temp += int(i)**2
            n = temp
            temp = 0
            print(n)
            
            if n == 1:
                return True
            elif n in created:
                return False
            else:
                created[n] = 1