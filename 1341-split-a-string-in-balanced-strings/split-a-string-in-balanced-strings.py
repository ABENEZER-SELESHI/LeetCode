class Solution:
    def balancedStringSplit(self, s: str) -> int:
        stack_l = []
        stack_r = []

        count = 0

        for char in s:
            if char == "L":
                stack_l.append(char)
            else:
                stack_r.append(char)
            # check balance
            if len(stack_l) == len(stack_r):
                count += 1
                stack_l = []
                stack_r = []
        return count
        