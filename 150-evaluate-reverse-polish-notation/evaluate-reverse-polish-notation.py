class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token.lstrip('-').isdigit():
                stack.append(int(token))
            else:
                right = stack.pop()
                left = stack.pop()
                
                if token == '+':
                    stack.append(left + right)
                elif token == '-':
                    stack.append(left - right)
                elif token == '*':
                    stack.append(left * right)
                elif token == '/':
                    stack.append(int(left / right))
                
        return stack[0]
        