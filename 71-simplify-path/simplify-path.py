class Solution:
    def simplifyPath(self, path: str) -> str:
        store = path.split("/")
        stack = []
        
        for char in store:
            if char == "..":
                if stack:
                    stack.pop()
            else:
                if char != "" and char != ".":
                    stack.append(char)
        # return stack
        res = "/"+"/".join(stack)
        
        return res
