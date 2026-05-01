class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return True
        
        if len(s) == 1:
            return False
        
        stack = []

        for bracket in s:
            if bracket == ']':
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append(bracket)
            
            elif bracket == '}':
                if stack and stack[-1] == "{":
                    stack.pop()
                else:
                    stack.append(bracket)

            elif bracket == ')':
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(bracket)       

            else:
                stack.append(bracket)
        
        return len(stack) == 0

