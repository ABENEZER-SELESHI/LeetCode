class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        count = 1
        while count > 0:
            if (count * n) % 2 == 0:
                return (count * n)
            count = count + 1