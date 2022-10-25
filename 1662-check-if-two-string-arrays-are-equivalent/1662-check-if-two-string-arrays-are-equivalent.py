class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        check1 = ''.join(word1)
        check2 = ''.join(word2)
        
        return check1 == check2