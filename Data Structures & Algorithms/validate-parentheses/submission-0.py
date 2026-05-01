class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to keep track of opening brackets
        stack = []
        
        # Hash map to keep track of mappings
        mapping = {")": "(", "}": "{", "]": "["}
        
        # For every bracket in the string
        for char in s:
            # If the character is a closing bracket
            if char in mapping:
                # Pop the topmost element from the stack, if it is non-empty
                # Otherwise, assign a dummy value of '#'
                top_element = stack.pop() if stack else '#'
                
                # The mapping for the closing bracket in the stack does not match the mapping
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, push it onto the stack
                stack.append(char)
        
        # If the stack is empty, all the brackets are closed correctly
        return not stack
            