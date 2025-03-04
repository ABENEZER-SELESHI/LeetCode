class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count("1")
        zeros = s.count("0")

        res = ""
        res += "1"*(ones-1)
        res += "0"*zeros
        res += "1"

        return res