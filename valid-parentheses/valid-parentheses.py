class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        charArr = [c for c in s]
        
        if(len(s) % 2 != 0):
            return False
        
        for c in charArr:
            if(c == "(" or c == "{" or c == "["):
                stack.append(c)
            elif(c == ")"):
                if(len(stack) == 0 or stack.pop() != "("):
                    return False
            elif(c=="}"):
                if(len(stack) == 0 or stack.pop() != "{"):
                    return False
            elif(c=="]"):
                if(len(stack) == 0 or stack.pop() != "["):
                    return False
        if(len(stack) != 0):
            return False
        return True
        