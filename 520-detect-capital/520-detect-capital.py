class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        #return re.fullmatch(r"[A-Z]*|.[a-z]*", word)
        return word.isupper() or word.islower() or word.istitle()