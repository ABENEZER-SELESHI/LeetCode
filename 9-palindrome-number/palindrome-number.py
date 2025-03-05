class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        length = len(num)
        if length <= 1:
                return True
        for i in range (length // 2):
            if num[i] != num[-(i+1)]:
                return False
        return True

        