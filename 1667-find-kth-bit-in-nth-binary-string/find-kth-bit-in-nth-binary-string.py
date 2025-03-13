class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s):
            s_list = []
            for char in s:
                if char == "1":
                    s_list.append("0")
                else:
                    s_list.append("1")
            s_list.reverse()
            return "".join(s_list)

        def rec(prev):
            if len(prev) > k:
                return prev[k-1]
            rev = invert(prev)
            s_list = [prev, "1", rev]
            word = "".join(s_list)
            return rec(word)
        return rec("0")

    
    