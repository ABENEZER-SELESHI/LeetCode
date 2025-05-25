class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ltr = [i for i, c in enumerate(s) if c.isalpha()]
        n = len(ltr)
        res = []

        for bits in range(1 << n):
            chars = list(s)
            for i in range(n):
                if bits & (1 << i):
                    chars[ltr[i]] = chars[ltr[i]].upper()
                else:
                    chars[ltr[i]] = chars[ltr[i]].lower()
            res.append(''.join(chars))

        return res