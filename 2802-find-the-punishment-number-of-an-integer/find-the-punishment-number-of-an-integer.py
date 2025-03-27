class Solution:
    def punishmentNumber(self, n: int) -> int:
        # return int("11")
        store = 0

        def equity(val, x, sm, ind):
            if ind == len(x):
                return val == sm
            # print(len(x))
            if len(x) > 1:
                for i in range(ind+1, len(x)+1):
                    # print(i)
                    s = int(x[ind:i])
                    # print(s)
                    if equity(val, x, sm + s, i):
                        return True
            return False
        # return equity(36, str(36*36), 0, 0)
        ptr = 1
        while ptr <= n:
            if ptr == 1:
                store += 1
            elif equity(ptr, str(ptr*ptr), 0, 0):
                store += (ptr*ptr)
            ptr += 1
        
        return store