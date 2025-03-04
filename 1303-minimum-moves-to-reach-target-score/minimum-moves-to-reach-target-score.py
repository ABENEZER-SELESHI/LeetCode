class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        store = 0

        

        # at full value
        while maxDoubles > 0:
            if target <= 3:
                store += target - 1
                return store
            if target % 2 == 0:
                store += 1
                target = target//2
            else:
                store += 2
                target = (target - 1)//2
            if target == 1:
                return store
            maxDoubles -= 1
        store += target-1
        return store