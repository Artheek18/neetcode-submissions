class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        stack = []

        for token in tokens:
            if stack and token in operators:
                opOne = int(stack.pop())
                opTwo = int(stack.pop())
                
                if token == "+":
                    stack.append(opTwo + opOne)

                elif token == "-":
                    stack.append(opTwo - opOne)

                elif token == "*":
                    stack.append(opTwo * opOne)
            
                else:
                    stack.append(int(opTwo / opOne))
            
            else:
                stack.append(int(token))

        return stack.pop()
