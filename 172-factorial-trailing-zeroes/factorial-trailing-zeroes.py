class Solution:
    def trailingZeroes(self, n: int) -> int:
        sys.set_int_max_str_digits(100000000)
        def rec(n):
            if n == 1 or n == 0:
                return 1
            x = rec(n-1)
            res = n * x
            return res

        val = str(rec(n))

        count = 0
        for i in range(len(val)-1, -1, -1):
            if val[i] != "0":
                return count
            count += 1
