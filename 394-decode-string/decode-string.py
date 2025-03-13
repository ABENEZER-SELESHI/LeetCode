class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != "]":
                stack.append(char)
            else:
                # the letters in bracket
                temp_list = []
                while stack[-1] != "[":
                    temp_list.append(stack.pop())
                stack.pop()
                
                temp = "".join(reversed(temp_list))
                
                # the number to multiply by
                mult_list = []
                while stack and stack[-1].isdigit():
                    mult_list.append(stack.pop())

                mult = int("".join(reversed(mult_list)))
                
                stack.append(temp * mult)

        return "".join(stack)
