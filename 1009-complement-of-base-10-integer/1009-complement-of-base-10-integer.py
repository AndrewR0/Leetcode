class Solution:
    def bitwiseComplement(self, n: int) -> int:
        
        nLen = len(bin(n)[2:])
        c = 0
        
        for i in range(nLen):
            c += 2**i
        
        
        return n ^ c