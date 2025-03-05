class Solution:
    def removeStars(self, s: str) -> str:
        store = []
        count = 0
        for char in s:
            if char != "*":
                store.append(char)
            else:
                store.pop()
        return "".join(store)

