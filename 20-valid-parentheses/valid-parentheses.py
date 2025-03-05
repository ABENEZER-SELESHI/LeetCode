class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in brackets:
                e = stack.pop() if stack else '#'
                
                if brackets[char] != e:
                    return False
            else:
                stack.append(char)
        return not stack
                    
        