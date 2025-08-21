class Solution:
    def isPalindrome(self, x: int) -> bool:
        wordNum = str(x)
        left = 0
        right = len(wordNum) - 1

        if x < 0 or len(wordNum) < 1:
            return False

        while left < right:
            if wordNum[left] != wordNum[right]:
                return False
            left += 1
            right -= 1
        return True

        